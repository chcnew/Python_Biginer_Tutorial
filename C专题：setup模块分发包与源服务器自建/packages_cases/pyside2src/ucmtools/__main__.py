#!/bin/bash/python3
# _*_ coding: utf-8 _*_

import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import ucmtools as models


def get_application_instance():
    """
    获取QT application单例

    :return: QApplication创建的实例
    """
    if not QApplication.instance():
        _app = QApplication(sys.argv)
    else:
        _app = QApplication.instance()
    return _app


def bool_widget():
    """bool_widget"""
    app = get_application_instance()
    window = QWidget()
    widget = models.BoolWidget(default=True, content="是否正确")
    widget.register(window)
    assert widget.target == window, "注册至父对象异常"
    assert widget.layout_style == "vertical", "布局设置功能异常"  # 默认布局
    widget.layout_style = "horizontal"
    assert widget.layout_style == "horizontal", "布局设置功能异常"
    assert widget.default == True, "默认值设置功能异常"
    assert widget.get_inbox_value() == True, "获取是否勾选值功能异常"
    assert widget.get_inbox_text() == "是否正确", "获取选项文本功能异常"
    widget.set_inbox_value(False)
    assert widget.get_inbox_value() == False, "获取是否勾选值功能异常"
    widget.set_inbox_text("设置文本")
    assert widget.get_inbox_text() == "设置文本", "获取选项文本功能异常"
    # region BoolWidget不涉及label功能(label已隐藏)，关闭相关函数功能(返回值为None)
    widget.set_hide_label_status(True)
    assert widget.get_hide_label_status() == True, "不涉及label功能，值默认为True，表示已隐藏"
    # 函数功能关闭，set_label_attr()、set_inbox_attr()将不生效
    widget.set_label_attr({"setFixedWidth": 400}), "设置Label相关属性错误"
    assert widget._ui.label.width() != 400, "不涉及label功能，值应为None"
    widget.set_label_attr({"setText": "属性方式设置"})
    assert widget.get_label_text() == "", "不涉及label功能，值应为空串"
    assert widget._ui.label.text() != "属性方式设置", "不涉及label功能，值应为None"
    # endregion
    widget.set_inbox_attr({"setFixedWidth": 400})
    assert widget._ui.check_box.width() == 400, "set_inbox_attr函数功能异常"
    widget.set_inbox_attr({"setChecked": True})
    assert widget.get_inbox_value() == True, "获取是否勾选值功能异常"

    # 测试不涉及的set_label_text函数
    assert widget.set_label_text("xxx") is None
    assert widget._ui.label.text() == "", "set_label_text函数不涉及情况应该"

    # widget.unregister()
    # assert widget.target is None
    # assert widget.registered == False

    window.show()
    app.exec_()


def openfile_widget():
    """OpenFileBoxWidget"""
    app = get_application_instance()
    window = QWidget()
    window1 = QWidget()
    widget = models.OpenFileBoxWidget(
        shape=[2, 2],
        verbose_name="File",
        titles=["Ftext1", "Ftext2"],
        default=["value1", "value2"],
        group_tf=False,
        button_text=["Select1", "Select2"]
    )
    widget.register(window)
    assert widget.get_label_text() == ["Ftext1", "Ftext2", "File", "File"], "获取label文本异常"
    assert widget.get_inbox_value() == ["value1", "value2", "", ""], "获取值异常"
    widget.set_inbox_value("value_all")
    assert widget.get_inbox_value() == ["value_all"] * 4, "获取值异常"
    widget.set_inbox_value("value_all_23", 2, 3)
    assert widget.get_inbox_value() == ["value_all", "value_all_23", "value_all_23", "value_all"], "获取值异常"

    widget1 = models.OpenFileBoxWidget(
        shape=[2, 2],
        verbose_name="File",
        titles=["Ftext1", "Ftext2"],
        default=["value1", "value2"],
        group_tf=False,
        button_text="Select"
    )
    widget1.register(window1)
    assert widget1.get_button_text() == ["Select"] * 4
    widget1.set_button_text("111,222", 1, 2)
    assert widget1.get_button_text() == ["111,222", "111,222", "Select", "Select"]
    widget1.set_button_attr({"setFixedWidth": 100})
    for i in range(4):
        assert widget1._widget_list[i]._ui.push_button.width() == 100
    window.show()
    app.exec_()


if __name__ == '__main__':
    openfile_widget()
