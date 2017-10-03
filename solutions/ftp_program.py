from ftplib import FTP



if __name__ == '__main__':

    ftpUrl = input('Please enter FTP url: ')
    ftp = FTP(ftpUrl)

    print('Connecting to FTP...')

    try:
        ftp.login()

    except Exception as e:
        print(str(e))

    ftp.retrlines('LIST')
