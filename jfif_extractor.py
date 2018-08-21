from sys import argv
START = '\xFF\xD8'
END = '\xFF\xD9'
ANOTHER_DATA_FILE_NAME = 'secret_data'
print '*' * 8 + ' Welcome the the wello\'s JFIF extractor! Expects only JPG files ' + '*' * 8

num_image = 0
if len(argv) == 2:
    try:
        with open(argv[-1],'rb') as binary_image:
            data = binary_image.read()
            if data.find(START) == -1 or data.find(END) == -1:
                print '[*] File is not JPG [*]'
                exit()
    except IOError:
        print '[*] File does not exist! [*]'
        exit()
    except Exception:
        print '[*] Unknown Error [*]'
        exit()

    while len(data) > 0:
        current = data.find(START), data.find(END)

        if current[0] == -1 and current[1] == -1:
            #Data that is not jpeg, but there is something
            print '[+] Something intersting! - `%s` [+]' % (ANOTHER_DATA_FILE_NAME)
            with open(ANOTHER_DATA_FILE_NAME, 'wb') as write_to:
                write_to.write(data)
                break #data has gone

        new_file_data = data[current[0]:current[1] + len(END)]
        if len(new_file_data) > (len(START) + len(END)):
            new_file_name = str(num_image) + '.jpg'
            print '[+] JFIF #%d  - %s [+]' % (num_image, new_file_name)
            num_image += 1

            with open(new_file_name, 'wb') as write_to:
                write_to.write(new_file_data)
            #print 'Length of data before: %d' % (len(data))

        data = data[data.find(END) + len(END):]
        #print 'Length of data after: %d' % (len(data))
        
else:
    print '[*] argv[2] should be the path to the JPEG [*]'
