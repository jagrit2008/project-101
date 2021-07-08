import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A0BHmfQIC84mKZ2Sl3YnVEJ0LdeCI7Nwr4WbPJrX1qRBCX9bipSQOBZpWPHTmeeDfR3eA0m4Xrs-i0XM3DyQgldXTjptsYImQXpPV3ZUveP0XF42O_bLAjn_0hvlGMVcRmZNRGs'
    transferData = TransferData(access_token)

    file_from = input("enter the file path to transfer:")
    file_to = input("Enter the full path to upload to dropbox:")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved.")
if __name__ == '__main__':
    main()