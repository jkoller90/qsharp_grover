from BitVector.BitVector import BitVector
import sys

e= 65537
#Prime Numbers generated using PrimeGenerator.py
p= 330794090188851917472427743832351209577
q= 324096243794776702990762793667764525999

def ReadFile(filename):
    binstring = ''
    #Read from message file
    text_file = open(filename, 'r')
    input_text = text_file.read()
    text_file.close()
    input_text = list(input_text)

    #Padding newlines to end of string
    while(len(input_text)%8!=0):
        input_text.append("\n")
    for i in input_text:
        binstring = binstring + ('{0:08b}'.format((ord(i))))
    return binstring

def WriteEncryptedFile(CipherText,filename):
    #Writing CipherText onto output file
    text_file = open(filename, "w")
    text_file.write(CipherText)
    text_file.close()

def ReadOutputFile(filename):
    #Read CipherText from output file
    text_file = open(filename, "r")
    EncryptedText=text_file.read()
    text_file.close()
    return EncryptedText

def WriteDecryptedFile(PlainText,filename):
    #Strip extra lines from String
    PlainText.strip('\n')
    text_file = open(filename, 'w')

    #Convert a String of 8 bits into its correspodning ASCII value
    for i in range(0, int(len(PlainText)/8)):
        text_file.write(chr(int(PlainText[(i*8):(i*8)+8],2)))
    text_file.close()

def ZeroPadding(BinaryString):
    paddedoutput=''

    #Pad 0s to the binary bits to ensure each block is 256 bits
    for i in range(0,10):
        for j in range(0,128):
            paddedoutput = paddedoutput + '0'
        paddedoutput = paddedoutput + BinaryString[(i*128):(i*128)+128]
    return paddedoutput

def Encryption(PaddedString):
    cipher=''
    for i in range(0,10):
        #Perform encryption for current block
        temp= bin(pow(int(PaddedString[i*256:(i*256)+256],2),e,(p*q)))
        #Remove Binary identifier to obtain plain binary string
        temp=temp.replace('0b','')
        while (len(temp)<256):
            temp='0'+temp
        cipher=cipher+temp
    return cipher

def Decryption(d, EncryptedText):
    final=''
    temp=1
    for i in range(0,10):
        #Decryption for current block
        temp = bin(pow(int(EncryptedText[i*256:(i*256)+256],2),d,(p*q)))
        #Remove Binary identifier to obtain plain binary string
        temp = temp.replace('0b', '')
        while(len(temp)<128):
            temp='0'+temp
        final=final+temp
    return final

def DecryptionKey():
    #Calculate the Decryption key d using BitVector function
    d = (BitVector.multiplicative_inverse(BitVector(intVal=e), BitVector(intVal=((p-1)*(q-1)))))
    return int(d)

def main():
    argList = sys.argv
    #When invalid arugments are provided
    if len(argList)!=4:
        print("Error! Please provide valid Arguments!")
        print('For Encryption, run as: python3 hw2.py -e \'inputfile\' \'outputfile\'')
        print('For Decryption, run as: python3 hw2.py -d \'inputfile\' \'outputfile\'')
        exit()

    #When Encryption arguements are passed
    if argList[1]=='-e':
        BinaryString = ReadFile(filename=argList[2])
        PaddedString =(ZeroPadding(BinaryString=BinaryString))
        CipherText = Encryption(PaddedString)
        WriteEncryptedFile(CipherText=CipherText, filename=argList[3])
        print("Encrption Completed. Please check the output file")

    #When Decryption arguments are passed
    elif argList[1]=='-d':
        EncryptedText= ReadOutputFile(filename=argList[2])
        d = DecryptionKey()
        PlainText = Decryption(d,EncryptedText=EncryptedText)
        WriteDecryptedFile(PlainText=PlainText, filename=argList[3])
        print("Decryption Completed. Please check the output file")

    else:
        print("Error! Please provide valid Arguments!")
        print('For Encryption, run as: python3 hw2.py -e \'inputfile\' \'outputfile\'')
        print('For Decryption, run as: python3 hw2.py -d \'inputfile\' \'outputfile\'')
if __name__ == '__main__':
    main()