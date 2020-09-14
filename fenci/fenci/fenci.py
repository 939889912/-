import jieba
from wordcloud import WordCloud
cd='功勋赫赫的长林军,遭遇到与赤焰军相似的处境,外有战斗力强劲的大渝,内有梁朝的朝臣和内奸作祟,非要将长林军置于死地。 长林比赤焰幸运的是,新梁帝不像他爷爷'
mytext = " ".join(jieba.cut(cd))
print(mytext)

wordcloud = WordCloud(font_path=r'D:\zhouty python project\自动分词\fenci\SimSun.ttf').generate(mytext)

import matplotlib.pyplot as plt
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()
