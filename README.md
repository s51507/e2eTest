# e2eTest for github login

## Description

```
1. run main.py

2. 打上github帳號密碼

```

## Funtions
```
wait：等待頁面元素出現，20秒沒出現的話會列出哪個元素無回應並擷取該畫面

click：等待頁面元素出現後點擊，目前透過script點擊，好處是不用捲動畫面也能點到下面的按鈕

login：進行登入流程

整個流程為：
1.使用者在cmd上輸入帳號密碼
(接下來的步驟皆由python自動完成)
2.開啟github首頁
3.點擊右上方Sign in
4.輸入帳號
5.輸入密碼
6.點擊Sign in
7.等待右上方帳號資訊顯示
8.Done

```

