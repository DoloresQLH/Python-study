print("===============================序列（01字符串）乘法运算示例===================")
sentence = input("Sentence:")  #输入字符串

screen_width = 80
text_width = len(sentence)  #获取输入字符串索引值 len()
print(text_width)
box_width = text_width + 6  #
print(box_width)
left_margin = (screen_width - box_width) // 2
print(left_margin)
print()
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print(' ' * left_margin + '| ' + ' ' * text_width + ' |')
print(' ' * left_margin + '| ' + sentence + ' |')
print(' ' * left_margin + '| ' + ' ' * text_width + ' |')
print(' ' * left_margin + '+' + '-' * (box_width-2) + '+')
print()