# Super Simple BRender KeyGen
Simple BRender SDK KeyGen.

![image](https://user-images.githubusercontent.com/26048525/149608517-f97e07c5-8b65-4b86-a724-4aba68244275.png)

## Info
This is just a super simple keygen for the BRender SDK installer coded in python.<br>
All testing was done with BRender SDK 1.2 so unsure of the compatibility with other BRender installers.<br>
The original python keygen was done by foon I think and can be found here along with the BRender SDK it's self.<br>
https://archive.org/details/brender25<br>
So I just took that code and pacadged it into something other people could run, <br>
and making it a little nicer and presentable at the same time.<br>

## Ramblings
I am unsure of minimum key length as the installer just seems to give you a random Identification code.<br>
If you do get an Identification code of less then 8 numbers, just close the installer and restart it<br>
and it will give you a new random Identification code. If it happens a lot then i'll adjust the keygen.<br>
Also sadly the BRenderKeygen(x64).exe is only for 64bit OS and will not run on 32bit OS..<br>
or win95 which is a 16bit OS. It's due to pyinstaller only building a 64bit exe as that's what I ran it on, a 64bit os.<br>
If I manage to find out how to set the output exe variables then I will make another build for 32bit.<br>
Don't think it could ever run on win95 but I would love to be proven wrong.<br>
It appears to be very simple math so can't imagine it be to hard to make a native c app for this and compile that<br>
for win 95, for now though python code is fine.<br>
