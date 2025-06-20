# YouTube Comment Crawler (Shorts supported)
<img width="501" alt="UI" src="https://github.com/user-attachments/assets/8718dc9f-8ff4-4c3b-bfc0-bdb30fe04cf7" />

유튜브 댓글을 엑셀로 저장해주는 파이썬 프로그램 입니다.

롱폼과 쇼츠 모두 지원하며, 크롬 브라우저와 함께 동작합니다.

![2025-06-2012 18 57-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/bc9124b3-d39f-482c-abf5-53ae83f77b9a)
실행을 위해 유튜브 URL과 저장 경로를 설정하여 시작 버튼을 누르면 크롬 브라우저가 실행되고 자동으로 스크롤이 움직여 댓글을 저장합니다.
(1.5초 당 댓글 20개)


## Contents
- [Prerequisites](#prerequisites)
- [Cautions](#cautions)
- [Quick Start](#quick-start)
- [Troubleshootings](#troubleshootings)


## Prerequisites
실행에 앞서, 아래 사항들을 확인해주세요.

Check prerequisites before you run.

### Install Chrome browser
해당 코드는 [크롬 브라우저](https://www.google.com/intl/ko_kr/chrome/)와 동작하도록 설계되어 있습니다.

따라서 크롬 브라우저를 설치한 뒤에 실행해주세요.
(단, 기본 브라우저로 설정하지 않으셔도 됩니다.)

This code works with [Chrome browser](https://www.google.com/intl/en/chrome/), thus, you need to install Chrome before you run.
(However, you don't need to set Chrome as default browser.)

### Download Python packages
아래 명령어를 실행하여 필요한 패키지들을 설치하세요.

Run a command for installing python packages.

```
$ pip install selenium pyautogui numpy pandas
```


## Cautions
실행 시 나타나는 크롬이 항상 화면 내에 보이도록 해주세요.

실행 도중에 다른 작업을 동시에 하는 것은 가능하지만, 실행 중인 크롬을 축소화 하거나 다른 화면을 전체보기로 하여 화면이 가려질 경우 댓글이 정상적으로 저장되지 않을 수 있습니다.

Let Chrome page to be shown on your screen.

You can do other works while crawling comments, but do not minimize the Chrome tab or to be shown the other screen with full screen mode to cover the Chrome tab.
This cuases incomplete comment crawling.


## Quick Start
파이썬 설치 없이 실행 가능한 파일을 아래 링크에 업로드 하였습니다.

You can download executive files(Windows, MacOS) by visiting the links.

Windows(10/11): https://drive.google.com/file/d/1hIxTFO1AKGw7mv-WOOe7NcpWOrDLQi6k/view?usp=sharing
MacOS: https://drive.google.com/file/d/1lKEkfbmket4A4ipivLVeBEqkJpC_-yzQ/view?usp=sharing

### How to run in MacOS
맥OS에서 해당 파일을 바로 압축 해제하여 실행하면 `파일이 손상`되었다는 메시지를 내보낼 수 있습니다.

이 에러는 확인되지 않은 앱에 대한 맥OS의 보안 정책 때문으로, 터미널을 실행하여 파일이 저장된 위치에서 아래 명령어를 입력하면 정상적으로 동작합니다 :P

It may occurs `file ` error, when you're running the app in MacOS.

This error is caused by Apple's security policy for preventing 

```
xattr -rd com.apple.quarantine youtube-crawler-mac.app
```


## Troubleshootings
댓글이 전부 저장이 안 됐는데도 끝났어요
- 실행 도중에 화면이 ... 

댓글이 없다고 나와요
- 10초 내에 유튜브 페이지가 로딩이 되지 않을 경우 발생할 수 있습니다. 인터넷 속도나 현재 실행 중인

저장된 댓글의 개수가 안 맞아요
- 유튜브 정책에 의해 검열되었거나 검증 중인 댓글이 포함되어 있을 수 있습니다.

URL에 붙어녛기가 안 돼요
- 현재 입력이 한글인 경우 발생할 수 있습니다.
- 