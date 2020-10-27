from cv2 import resize

def crop(img, kind='center'):
    s = img.shape
    if s[0] < s[1]:
        c = s[1]//2 - s[0]//2
        return img[:, c : c+s[0]]
    else:
        c = s[0]//2 - s[1]//2
        return img[ c : c+s[1], :]
    
def euclidean_dist(a,b):
    l=(a[0]-b[0], a[1]-b[1])
    return (l[0]**2 + l[1]**2)**0.5

def preprocess_img(img, res=(360,360)):
    img = crop(img)
    img = resize(img, res)

    return img