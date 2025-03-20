# loggingLearning

Python日志模块logging



## 01.基本介绍(日志级别及其含义)

日志是跟踪软件运行时所发生的事件的一种方法。软件开发者在代码中调用日志函数，表明发生了特定的事件。事件由描述性消息描述，该描述性消息可以可选地包含可变数据（即，对于事件的每次出现都潜在地不同的数据）。事件还具有开发者归因于事件的重要性；重要性也可以称为级别或严重性。

logging提供了一组便利的函数，用来做简单的日志。它们是 debug()、 info()、 warning()、 error() 和 critical()。

logging函数根据它们用来跟踪的事件的级别或严重程度来命名。标准级别及其适用性描述如下（以严重程度递增排序）：

```reStructuredText
级别	何时使用
DEBUG	详细信息，一般只在调试问题时使用。
INFO	证明事情按预期工作。
WARNING	某些没有预料到的事件的提示，或者在将来可能会出现的问题提示。例如：磁盘空间不足。但是软件还是会照常运行。
ERROR	由于更严重的问题，软件已不能执行一些功能了。
CRITICAL	严重错误，表明软件已不能继续运行了。
```



| 级别       | 数字值 |
| :--------- | :----- |
| `CRITICAL` | 50     |
| `ERROR`    | 40     |
| `WARNING`  | 30     |
| `INFO`     | 20     |
| `DEBUG`    | 10     |
| `NOTSET`   | 0      |

默认等级是`WARNING`，这意味着仅仅这个等级及以上的才会反馈信息，除非logging模块被用来做其它事情。

被跟踪的事件能以不同的方式被处理。最简单的处理方法就是把它们在控制台上打印出来。另一种常见的方法就是写入磁盘文件。





## 02.利用logging.basicConfig()保存log到文件

```
logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    filename='new.log',
                    filemode='a',  ##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    # a是追加模式，默认如果不写的话，就是追加模式
                    format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'  # 日志格式
                    )
```





## 03.往屏幕输入，也往文件写入log

logging库采取了模块化的设计，提供了许多组件：记录器、处理器、过滤器和格式化器。

- Logger 暴露了应用程序代码能直接使用的接口。
- Handler将（记录器产生的）日志记录发送至合适的目的地。
- Filter提供了更好的粒度控制，它可以决定输出哪些日志记录。
- Formatter 指明了最终输出中日志记录的布局。

### **Loggers**

Logger 对象要做三件事情。首先，它们向应用代码暴露了许多方法，这样应用可以在运行时记录消息。其次，记录器对象通过严重程度（默认的过滤设施）或者过滤器对象来决定哪些日志消息需要记录下来。第三，记录器对象将相关的日志消息传递给所有感兴趣的日志处理器。

常用的记录器对象的方法分为两类：配置和发送消息。

这些是最常用的配置方法：

Logger.setLevel()指定logger将会处理的最低的安全等级日志信息, debug是最低的内置安全等级，critical是最高的内建安全等级。例如，如果严重程度为INFO，记录器将只处理INFO，WARNING，ERROR和CRITICAL消息，DEBUG消息被忽略。
Logger.addHandler()和Logger.removeHandler()从记录器对象中添加和删除处理程序对象。处理器详见Handlers。
Logger.addFilter()和Logger.removeFilter()从记录器对象添加和删除过滤器对象。

### **Handlers**

**处理程序**对象负责将适当的日志消息（基于日志消息的严重性）分派到处理程序的指定目标。`Logger` 对象可以通过`addHandler()`方法增加零个或多个handler对象。举个例子，一个应用可以将所有的日志消息发送至日志文件，所有的错误级别（error）及以上的日志消息发送至标准输出，所有的严重级别（critical）日志消息发送至某个电子邮箱。在这个例子中需要三个独立的处理器，每一个负责将特定级别的消息发送至特定的位置。

**最常用的有4种：** 

```
\1)   logging.StreamHandler -> 控制台输出 
使用这个Handler可以向类似与sys.stdout或者sys.stderr的任何文件对象(file object)输出信息。
它的构造函数是：
StreamHandler([strm])
其中strm参数是一个文件对象。默认是sys.stderr


\2)  logging.FileHandler -> 文件输出
和StreamHandler类似，用于向一个文件输出日志信息。不过FileHandler会帮你打开这个文件。它的构造函数是：
FileHandler(filename[,mode])
filename是文件名，必须指定一个文件名。
mode是文件的打开方式。默认是’a'，即添加到文件末尾。


\3)  logging.handlers.RotatingFileHandler -> 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件 
这个Handler类似于上面的FileHandler，但是它可以管理文件大小。当文件达到一定大小之后，它会自动将当前日志文件改名，然后创建 一个新的同名日志文件继续输出。比如日志文件是chat.log。当chat.log达到指定的大小之后，RotatingFileHandler自动把 文件改名为chat.log.1。不过，如果chat.log.1已经存在，会先把chat.log.1重命名为chat.log.2。。。最后重新创建 chat.log，继续输出日志信息。它的构造函数是：
RotatingFileHandler( filename[, mode[, maxBytes[, backupCount]]])
其中filename和mode两个参数和FileHandler一样。
maxBytes用于指定日志文件的最大文件大小。如果maxBytes为0，意味着日志文件可以无限大，这时上面描述的重命名过程就不会发生。
backupCount用于指定保留的备份文件的个数。比如，如果指定为2，当上面描述的重命名过程发生时，原有的chat.log.2并不会被更名，而是被删除。


\4)  logging.handlers.TimedRotatingFileHandler -> 按照时间自动分割日志文件 
这个Handler和RotatingFileHandler类似，不过，它没有通过判断文件大小来决定何时重新创建日志文件，而是间隔一定时间就 自动创建新的日志文件。重命名的过程与RotatingFileHandler类似，不过新的文件不是附加数字，而是当前时间。它的构造函数是：
TimedRotatingFileHandler( filename [,when [,interval [,backupCount]]])
其中filename参数和backupCount参数和RotatingFileHandler具有相同的意义。
interval是时间间隔。
when参数是一个字符串。表示时间间隔的单位，不区分大小写。它有以下取值：
S 秒
M 分
H 小时
D 天
W 每星期（interval==0时代表星期一）
midnight 每天凌晨
```



配置方法：

- `setLevel()`方法和日志对象的一样，指明了将会分发日志的最低级别。为什么会有两个`setLevel()`方法？记录器的级别决定了消息是否要传递给处理器。每个处理器的级别决定了消息是否要分发。
- `setFormatter()`为该处理器选择一个格式化器。
- `addFilter()`和`removeFilter()`分别配置和取消配置处理程序上的过滤器对象。

Formatters

Formatter对象设置日志信息最后的规则、结构和内容，默认的时间格式为%Y-%m-%d %H:%M:%S，下面是Formatter常用的一些信息

| %(name)s            | Logger的名字                                                 |
| ------------------- | ------------------------------------------------------------ |
| %(levelno)s         | 数字形式的日志级别                                           |
| %(levelname)s       | 文本形式的日志级别                                           |
| %(pathname)s        | 调用日志输出函数的模块的完整路径名，可能没有                 |
| %(filename)s        | 调用日志输出函数的模块的文件名                               |
| %(module)s          | 调用日志输出函数的模块名                                     |
| %(funcName)s        | 调用日志输出函数的函数名                                     |
| %(lineno)d          | 调用日志输出函数的语句所在的代码行                           |
| %(created)f         | 当前时间，用UNIX标准的表示时间的浮 点数表示                  |
| %(relativeCreated)d | 输出日志信息时的，自Logger创建以 来的毫秒数                  |
| %(asctime)s         | 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒 |
| %(thread)d          | 线程ID。可能没有                                             |
| %(threadName)s      | 线程名。可能没有                                             |
| %(process)d         | 进程ID。可能没有                                             |
| %(message)s         | 用户输出的消息                                               |

 

**案例需求：**

输出log到控制台以及将日志写入log文件。
保存2种类型的log， all.log 保存debug, info, warning, critical 信息， error.log则只保存error信息，同时按照时间自动分割日志文件。

![复制代码](loggingLearning/copycode.gif)

```
import logging
from logging import handlers

class Logger(object):
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射

    def __init__(self,filename,level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)
if __name__ == '__main__':
    log = Logger('all.log',level='debug')
    log.logger.debug('debug')
    log.logger.info('info')
    log.logger.warning('警告')
    log.logger.error('报错')
    log.logger.critical('严重')
    Logger('error.log', level='error').logger.error('error')
```