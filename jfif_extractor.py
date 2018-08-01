from sys import argv
START = '\xFF\xD8'
END = '\xFF\xD9'

print '*' * 8 + ' Welcome the the wello\'s JFIF extractor! Expects only JPG files ' + '*' * 8

num_image = 0
if len(argv) == 2:
    try:
        with open(argv[-1],'rb') as binary_image:
            data = binary_image.read()
            if data.find(START) == -1:
                print '[*] File is not JPG [*]'
                exit()
    except IOError:
        print '[*] File does not exist! [*]'
        exit()
    except:
        print '[*] Unknown Error [*]'
        exit()

    while len(data) > 0:
        current = data.find(START), data.find(END)
        #print current
        new_file_data = data[current[0]:current[1]]
        new_file_name = str(num_image) + '.jpg'
        print '[+] JFIF #%d  - %s [+]' % (num_image, new_file_name)
        with open(new_file_name, 'wb') as write_to:
            write_to.write(new_file_data)
        #print 'Length of data before: %d' % (len(data))
        data = data[data.find(END) + len(END):]
        #print 'Length of data after: %d' % (len(data))
        num_image += 1
else:
    print '[*] NOT ENOUGH PARAMS! [*]'
