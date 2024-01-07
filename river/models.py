# By: shawn@chaoo.ltd

from django.db import models
# django.db.models.functions import Now
#选择模型
class Choice(models.Model):
    CATEGORIES = {
        ("A",u"审批条件"), #审批条件
        ("B",u"分支条件")   #分支条件
    }
    name = models.CharField(u"选择", max_length=60)
    category = models.CharField(u"分类", max_length=1, choices=CATEGORIES)
    pub_date = models.DateTimeField("更新时间", auto_now=True)

#逻辑模型
class Logic(models.Model):
    name = models.CharField(max_length=60)
    pub_date = models.DateTimeField("更新时间", auto_now=True)
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)


#条件模型
class Condition(models.Model):
    choice = models.IntegerField(default=0)
    logic = models.IntegerField(default=0)
    val = models.IntegerField(default=0)
    pub_date = models.DateTimeField("更新时间", auto_now=True)

#审批节点模型
class ApproveNode(models.Model):
    #0=审批节点，1=分支节点，2=抄送节点, 3=默认(兜底)节点
    NODETYPE = {
        ("A", u"审批节点"),  #审批节点
        ("B", u"分支节点"),  #分支节点
        ("C", u"抄送节点"),  #抄送节点
        ("D", u"默认节点")   #默认节点
    }
    CONTYPE = {
        ("A", u"且"),  #条件间关系：且，或
        ("B", u"或") 
    }
    LOGICTYPE = {
        ("A",u"会签"),
        ("B",u"或签")
    }
    name = models.CharField("节点名称", max_length=60)
    type = models.CharField(max_length=1, choices=NODETYPE)
    parents = models.ForeignKey(
        "ApproveNode",
        on_delete=models.CASCADE,
    )
    contype = models.CharField(max_length=1, choices=CONTYPE)
    logictype = models.CharField(max_length=1, choices=LOGICTYPE)
    conditions = models.ForeignKey(
        "Condition",
        on_delete=models.CASCADE,
    )
    endnode = models.BooleanField(default=False)
    childid = models.IntegerField(default=0)
    pub_date = models.DateTimeField("更新时间", auto_now=True)