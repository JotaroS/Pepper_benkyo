import cv2

src = cv2.imread("../petitcom-kbd-fix.png", 1)
tmp = cv2.imread("../petit-kbd-1.png", 1)

res = cv2.matchTemplate(src, tmp, cv2.TM_CCOEFF_NORMED)

(minval, maxval, minloc, maxloc) = cv2.minMaxLoc(res)

print "({0}, {1}) score = {2}\n".format(maxloc[0], maxloc[1], maxval)

(h, w, d) = tmp.shape

rect_1 = (maxloc[0], maxloc[1])
rect_2 = (maxloc[0] + w, maxloc[1] + h)
print "({0}, {1}) score = {2}\n".format(maxloc[0], maxloc[1], maxval)
print "size ({0}, {1})\n".format(w, h)
cv2.rectangle(src, rect_1, rect_2, 0x00ff00)

cv2.imwrite("py-output.png", src)
