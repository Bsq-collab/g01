with open("image.ppm", "w") as f:
    #data = f.read()
    f.seek(0)
    f.write("P3\n")
    f.write("500 500\n")
    f.write("255\n")

    for row in range(500):
        text=""
        r= row % 255
        b=0
        g= 255* row/333
        c=0;
        for col in range(500):
            text+=str(r)+" "+str(col)+" "+ str(col%255)+ " "
        f.write(text+"\n")
