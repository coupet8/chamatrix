from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import matrix

def add_text(image):
    text_color = (0,0,0)
    anchor = 'mm'
    img = Image.open(image)
    draw = ImageDraw.Draw(img)

    # Координаты точек вставки текста
    pos_a = (95, 677)
    pos_b = (670, 115)
    pos_c = (1225, 680)
    pos_d = (664, 1236)
    pos_e = (662, 680)
    pos_f = (259, 275)
    pos_g = (1063, 275)
    pos_h = (1063, 1064)
    pos_i = (259, 1064)
    pos_j = (279, 677)
    pos_k = (199, 677)
    pos_l = (1046, 677)
    pos_m = (1124, 677)
    pos_n = (670, 299)
    pos_o = (665, 1055)
    pos_p = (670, 219)
    pos_r = (670, 1133)
    pos_s = (952, 952)
    pos_t = (911, 911)
    pos_u = (871, 871)
    pos_v = (465, 485)
    pos_x = (427, 445)
    pos_z = (385, 405)

    pos_af1 = (114, 458)
    pos_af2 = (88,541)
    pos_af3 = (152, 384)
    pos_af4 = (100, 499)
    pos_af5 = (130, 421)
    pos_af6 = (79, 589)
    pos_af7 = (173, 352)
    pos_a_f = [pos_af6, pos_af2, pos_af4, pos_af1, pos_af5, pos_af3, pos_af7]

    pos_fb1 = (433, 130)
    pos_fb2 = (352, 172)
    pos_fb3 = (514, 102)
    pos_fb4 = (387, 152)
    pos_fb5 = (473, 115)
    pos_fb6 = (316, 197)
    pos_fb7 = (559, 92)
    pos_f_b = [pos_fb6, pos_fb2, pos_fb4, pos_fb1, pos_fb5, pos_fb3, pos_fb7]

    pos_bg1 = (903, 131)
    pos_bg2 = (815, 101)
    pos_bg3 = (983, 173)
    pos_bg4 = (857, 113)
    pos_bg5 = (944, 151)
    pos_bg6 = (767, 91)
    pos_bg7 = (1019, 198)
    pos_b_g = [pos_bg6, pos_bg2, pos_bg4, pos_bg1, pos_bg5, pos_bg3, pos_bg7]

    pos_gc1 = (1217, 451)
    pos_gc2 = (1172, 364)
    pos_gc3 = (1245, 537)
    pos_gc4 = (1194, 402)
    pos_gc5 = (1232, 493)
    pos_gc6 = (1144, 322)
    pos_gc7 = (1254, 584)
    pos_g_c = [pos_gc6, pos_gc2, pos_gc4, pos_gc1, pos_gc5, pos_gc3, pos_gc7]

    pos_ch1 = (1219, 898)
    pos_ch2 = (1245, 815)
    pos_ch3 = (1177, 973)
    pos_ch4 = (1233, 859)
    pos_ch5 = (1202, 936)
    pos_ch6 = (1254, 772)
    pos_ch7 = (1148, 1026)
    pos_c_h = [pos_ch6, pos_ch2, pos_ch4, pos_ch1, pos_ch5, pos_ch3, pos_ch7]

    pos_hd1 = (905, 1222)
    pos_hd2 = (978, 1184)
    pos_hd3 = (815, 1253)
    pos_hd4 = (940, 1205)
    pos_hd5 = (860, 1240)
    pos_hd6 = (1013, 1160)
    pos_hd7 = (772, 1262)
    pos_h_d = [pos_hd6, pos_hd2, pos_hd4, pos_hd1, pos_hd5, pos_hd3, pos_hd7]

    pos_di1 = (424, 1220)
    pos_di2 = (512, 1251)
    pos_di3 = (341, 1174)
    pos_di4 = (465, 1236)
    pos_di5 = (382, 1198)
    pos_di6 = (560, 1262)
    pos_di7 = (303, 1146)
    pos_d_i = [pos_di6, pos_di2, pos_di4, pos_di1, pos_di5, pos_di3, pos_di7]

    pos_ia1 = (118, 905)
    pos_ia2 = (154, 978)
    pos_ia3 = (91, 824)
    pos_ia4 = (134, 941)
    pos_ia5 = (103, 866)
    pos_ia6 = (178, 1015)
    pos_ia7 = (82, 784)
    pos_i_a = [pos_ia6, pos_ia2, pos_ia4, pos_ia1, pos_ia5, pos_ia3, pos_ia7]

    # Объединение текста в группы в зависимости от размера круга (текста)
    pos_a_i = [pos_a, pos_b, pos_c, pos_d, pos_e, pos_f, pos_g, pos_h, pos_i]
    pos_j_r = [pos_j, pos_k, pos_l, pos_m, pos_n, pos_o, pos_p, pos_r]
    pos_s_z = [pos_s, pos_t, pos_u, pos_v, pos_x, pos_z]
    pos_4 = [pos_a_f, pos_f_b, pos_b_g, pos_g_c, pos_c_h, pos_h_d, pos_d_i, pos_i_a]

    # добавляем текст
    for i in range(len(pos_a_i)):
        font = ImageFont.truetype('arial.ttf', 52)
        draw.text(pos_a_i[i], str(matrix.matrix_a_i[i]), text_color, font, anchor)
    for i in range(len(pos_j_r)):
        font = ImageFont.truetype('arial.ttf', 42)
        draw.text(pos_j_r[i], str(matrix.matrix_j_r[i]), text_color, font, anchor)
    for i in range(len(pos_s_z)):
        font = ImageFont.truetype('arial.ttf', 30)
        draw.text(pos_s_z[i], str(matrix.matrix_s_z[i]), text_color, font, anchor)
    for i in range(len(pos_4)):
        for j in range(len(pos_4[i])):
            font = ImageFont.truetype('arial.ttf', 24)
            draw.text(pos_4[i][j], str(matrix.matrix_4[i][j]), text_color, font, anchor)
    # сохраняем новое изображение
    img.save('matrix_with_text.png')