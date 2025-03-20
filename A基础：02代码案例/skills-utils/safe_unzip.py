import os
import zipfile
import psutil


class MyZip:
    # 限制解压后大小不能超过1M，文件个数不能超过10个
    MAX_SIZE = 1 * 1024 * 1024
    MAX_FILE_CNT = 10

    @staticmethod
    def unzip(path, zip_file,MAX_SIZE=1 * 1024 * 1024,MAX_FILE_CNT = 10):
        file_path = path + os.sep + zip_file
        dest_dir = path
        src_file = zipfile.ZipFile(file_path, 'r')

        # 1.检查文件个数，文件个数大于预期值时上报异常退出
        file_count = len(src_file.infolist())
        if file_count >= MyZip.MAX_FILE_CNT:
            raise IOError(f'zipfile({zip_file}) contains {file_count} files exceed max file count')

        # 2.检查第一层解压文件总大小，总大小超过设定的上限值
        total_size = sum(info.file_size for info in src_file.infolist())
        if total_size >= MyZip.MAX_SIZE:
            raise IOError(f'zipfile({zip_file}) size({total_size}) exceed max limit')

        # 3.检查第一层解压文件总大小，总大小超过磁盘剩余空间
        dest_dir_partition = '/'  # 解压目录所在分区
        if total_size >= psutil.disk_usage(dest_dir_partition).free:
            raise IOError(f'zipfile({zip_file}) size({total_size}) exceed remain target disk space')

        # 4.解压所有文件
        src_file.extractall(dest_dir)
