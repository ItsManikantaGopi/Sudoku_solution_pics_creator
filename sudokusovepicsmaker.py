from PIL import ImageDraw as imd,Image as im,ImageFont 
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j],end=" ")
        print()
def row_find(arr,r,num):
    for i in range(9):
        if(arr[r][i]==num):
            return True
    return False
def col_find(arr,c,num):
    for i in range(9):
        if(arr[i][c]==num):
            return True
    return False
def box_find(arr,r,c,num):
    for i in range(3):
        for j in range(3):
            if(arr[i+r][j+c]==num):
                return True
    return False
def find_empty(arr,l):
    for i in range(9):
        for j in range(9):
            if(arr[i][j]==0):
                l[0]=i
                l[1]=j
                return True
    return False
def is_safe(arr,r,c,num):
    return not col_find(arr,c,num) and not row_find(arr,r,num) and not box_find(arr,r-r%3,c-c%3,num)
def sudo(arr):
    l=[0,0]
    if(not find_empty(arr,l)):
        return True
    r=l[0]
    c=l[1]
    for num in range(1,10):
        if(is_safe(arr,r,c,num)):
            arr[r][c]=num
            if(sudo(arr)):
                return True
            arr[r][c]=0
    return False
def pic(arr,st):
    img=im.new("RGB",(500,500),color="white")
    #fnt=ImageFont.truetype("FreeMono.ttf",40)
    draw=imd.Draw(img)
    x_start=y_start=0
    x_end=a=img.width
    y_end=b=img.height
    a=a/9
    b=b/9
    r=c=15
    for i in arr:
        c=15
        for j in i:
            draw.text((r,c),str(j),fill="black")
            c+=int(b)
        r+=int(a)
    for x in range(0,x_end,int(a)):
        draw.line(((x,y_start),(x,y_end)),fill="black")
    for y in range(0,y_end,int(b)):
        draw.line(((x_start,y),(x_end,y)),fill="black")   
    del draw
    img.save(st+".png")
    img.show()
def college(im_list):
	for n in range(len(im_list)):
		img=im.open(im_list[n])
		img.thumbnail((300,300))
		if(n%64==0):
			trget_img=im.new("RGB",(600,300),color="yellow")
		i=int(n/6)
		j=n%3
		trget_img.paste(img,(100*i,100*j))
	trget_img.show()

arr=[ [3,0,6,5,0,8,4,0,0], 
      [5,2,0,0,0,0,0,0,0], 
      [0,8,7,0,0,0,0,3,1], 
      [0,0,3,0,1,0,0,8,0], 
      [9,0,0,8,6,3,0,0,5], 
      [0,5,0,0,9,0,6,0,0], 
      [1,3,0,0,0,0,2,5,0], 
      [0,0,0,0,0,0,0,7,4], 
      [0,0,5,2,0,6,3,0,0]] 
pic(arr,"unsolved")
sudo(arr)
pic(arr,"solved")
l=["unsolved.png","solved.png"]
#l=["solved.png"]
college(l)
