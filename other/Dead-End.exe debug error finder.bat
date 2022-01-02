:: This batch file is used for essentially running the Dead-End.exe file in debug mode since this will output any
:: crash errors the exe file produces. This is helpful for debugging the exe file since if you run the exe without
:: this batch file, then the exe could have a crash error and the command prompt will exit too fast for you to read any
:: errors or bugs.
cd ..
Dead-End.exe
Pause