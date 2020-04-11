# Flutter

Flutter is an UI software development kit created by google. Flutter allows for fast creation of mobile apps. Supported platforms include but are not limited to Windows, Mac, Linux, iOS, and Android. [Full video tutorial](https://www.youtube.com/watch?v=2tmAQ3RGh1w) on Youtube.

## pre-required Software

you will need to have both **Git Bash** and **Visual Code** for this project. **Note:** *My visual Studio Code might look different than yours due to my dark pink theme.* 

### Software Download Links
- [Git bash for Windows](https://gitforwindows.org/)
- [Git bash for MacOS](https://git-scm.com/download/mac)
- [Visual Studio Code](https://code.visualstudio.com/)


## Installing Flutter SDK

You can simpy install flutter using their main web page and following the directions according to platform you are developing in.

### **Flutter Download Links-**
- [Flutter for Windows](https://flutter.dev/docs/get-started/install/windows)
- [Flutter for MacOS](https://flutter.dev/docs/get-started/install/macos)
- [Flutter for Linux](https://flutter.dev/docs/get-started/install/linux)
- [Andriod Studio](https://developer.android.com/studio)

## Fluter Console

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Flutter%20images/Flutter%20cmd.JPG)

## Flutter Doctor and Setup

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Flutter%20images/Flutter%20Doctor.JPG)

The **Flutter Doctor** will check if you are ready to start developing in 5 different platforms and if a smartphone is connected.

**Platform IDEs-**
- **Microsoft Windows**
- **Android toolchain**
- **Android Studio**
- **IntelliJ**
- **Visual Studio Code**

you can use **Flutter Doctor** by *typing* on the **Flutter Console**. 

```
flutter doctor
```

If you see that any of the section is not checked or has a red x, follow the instuctions provided to install into which ever platoform you wish to develope on.

For this project, we will be developing on **Visual Studio Code**. Most likely Flutter Doctor will indicate that **Visual Studio code** is not ready for Flutter development. We will need to download an extension.

## Installing Flutter Extension From Visual Studio Market
To download the Visual Studio Flutter Extension from the Market, it can be easily downloaded with the provided link.
[Visual Studio Flutter Extension](https://marketplace.visualstudio.com/items?itemName=Dart-Code.flutter)

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Flutter%20images/VS%20Flutter%20Extension.JPG)

Once you click **Download** you will be prompted to be redirected to Visual Studio Code; Confirm this action.

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Flutter%20images/VS%20Extension%20Download.JPG)

Visual Studio Code will redirect you to the proper installation page. click **Install** to add the extension to your Visual Studio IDE. 

## Installing Flutter directly from Vistual Studio Code

If for whatever reason you cannot visit the Visual Studio Market, we can still install Flutter's Dart Code from Visual Studio Code itself.

*Open* **Visual Studio Code**.

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Flutter%20images/blank%20studio%20workspace.JPG)

Navigate to **View** >> **command Palette**

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Flutter%20images/Command%20Palette.JPG)

Although we did install the Flutter Extension, We must also install the **Flutter Dart Code** 

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Flutter%20images/Install%20Extensions.JPG)

*type* "**install**" in the search box and options should start to become available. We are going to *click* **Extensions: Install Extensions**

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Flutter%20images/Flutter%20Dart%20Code.JPG)

In the new search box *type* "**Flutter**" and click on the first option. A new flutter page should open up and look similar to the first section that we downloaded. This is the Flutters Dart Code. click **Install** to add the extension to your Visual Studio IDE.

## Flutter: My First Application

To create a New Flutter Project. Navigate back to **view**>>**comand palette** and *type* **Flutter**.

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Flutter%20images/Flutter%20new%20project.JPG)

Next, we will name and save the application whatever we choose. **Note:** *application names must all be lowercase.

Once you decide where the project will be created and stored, **Flutter** will generate all the neccesary packets to creating an app. If all is done correctly, your **Visual Studio Code** should look like this.

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Flutter%20images/myapp%20created.JPG)

Although this may seem intimidating, Flutter has handled all of the packets in the background. We will be mostly using and editing **main.dart** file.

To test run our **main.dart** we must first select what device or emulation device we will perform on. In the bottom left corner, We will select the Android Smartphone we connected earlier. 

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Flutter%20images/Android%20Emulator.JPG)

Now with the target smartphone select we can hit DeBug and run. 

![image](https://raw.githubusercontent.com/jordanadrianoo/Hack-Quarantine-2020/master/Repository%20Images/Flutter%20images/App%20Demo.JPG=250x250)




