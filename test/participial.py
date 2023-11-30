# -*- coding: utf-8 -*-

import hanlp

hanlp_engine = hanlp.load(
    hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH
)


def test_participle():
    """分词"""

    sentence = "晚的发布会短安的发布会回到这个快国庆放假了才来开着小米西米二心米报位好多用户呢，也特别的期待我们的新产品在我的微博啊，日常催灯CV二不对吧，哎，我们自询数马君死时拿天天追求手机性能参数，而像你们这种猪打自拍的基比有什么好的脸好看好像还是挺有道理了，谢谢大家哎呀，不是脸的发布会还是赶紧把新机大出来吧，好看又好用在我们的全新息比二就搭载了一块六点五音寸局面频用为一百二之后自造精率和高频比到的特别高的功能听上去就很的三狂倍色丁萌经和外。你好猫合作的小白裙特别保安感觉整个人的气质都会提升我总机也只有七点二三毫米的后度一百七十一点八克的重量并保程度直接掉到了安卓不愿意做度性名苹果IPON只是却顶冰评的上狂激情非常轻也非常薄，那这时候就有聪明的形神不要问了哎呀，为什么做的这么薄呀，实在是太长了有的人五六个小时有的人甚至八九个小时我自己的痛感就是非常强烈的。"

    result = hanlp_engine(sentence, tasks="tok/fine").get("tok/fine")
    print(result)


test_participle()
