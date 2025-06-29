---
layout: post
title: Website Debugging
date: 2000-01-01 00:01 +0800
last_modified_at: 2099-12-31 23:59:59 +0800
categories: [X]
tags: [X]
toc: true
math: true
---
The content here should be displayed inside .message
{: .message }

This is a website debugging article. It is responsible for debugging various syntax/plugins/images. It will be pinned when necessary.

# MARKDOWN Basic Syntax

## Title Syntax

```markdown
# Level 1 heading
## Level 2 heading
### Level 3 heading
#### Level 4 heading
##### Level 5 heading
###### Level 6 heading
```

Printing Output

# Level 1 heading

## Level 2 heading

### Level 3 heading

#### Level 4 heading

##### Level 5 heading

###### Level 6 heading

## Literal Style Syntax

### Normal Font Effect 

```markdown
*Italic words*  
**Bold words**  
***Bold and italic words***
```

Printing Output

*Italic words*  
**Bold words**  
***Bold and italic words***

---

### Mathematical Formula Syntax

Use `math: true` to use them

```markdown
$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$
```

$$x = {-b \pm \sqrt{b^2-4ac} \over 2a}.$$

---

## List Syntax

### Ordered List

```markdown
1. First
2. Second
3. Third
4. Fourth
```

Printing Output

1. First
2. Second
3. Third
4. Fourth

---

### Unordered List

```markdown
- First
- Second
- Third
- Fourth
```

Printing Output

- First
- Second
- Third
- Fourth

## Block

### Quote Block

```markdown
> Words in blockquotes  
> **Bold words in blockquote**  
> - unordered list 1 in blockquote
> - unordered list 2 in blockquote
>
> 1. ordered list 1 in block reference
> 2. ordered list 1 in block reference
>
>> References in block references
>>> Duplicate references many times
```

Printing Output

> Words in blockquotes  
> **Bold words in blockquote**  
> - unordered list 1 in blockquote
> - unordered list 2 in blockquote
>
> 1. ordered list 1 in block reference
> 2. ordered list 1 in block reference
>
>> References in block references
>>> Duplicate references many times

---

### Code Block-1

    public class Demo {
        public static void main(String[] args) {
            System.out.println("Demo Code");
        }
    }

Printing Output


``` java
public class Demo {
    public static void main(String[] args) {
        System.out.println("Demo Code");
    }
}
```


---

### Code Block-2

```markdown
    This is also a code block.
	Four spaces are used before the text to create it.
```

Printing Output

    This is also a code block.
	Four spaces are used before the text to create it.

---

### Code Syntax

```markdown
This is `code`  
``Use `code` in Markdown``
```

Printing Output

This is `code`  
``Use `code` in Markdown``

## Other Syntax

### Separator Syntax

```markdown
There is a dividing line below this line of text

---

There is a dividing line above this line of text
```

Printing Output

There is a dividing line below this line of text

---

There is a dividing line above this line of text

**To ensure correct display, please add blank lines before and after the separator line.**

---

### Link Syntax

```markdown
Link [Ganfan_man's personal blog](https://gan-fan-man.github.io)

Link containing title [Google](https://google.com "Google search")

<https://gan-fan-man.github.io>
```

Printing Output

Link [Ganfan_man's personal blog](https://gan-fan-man.github.io)

Link containing title [Google](https://google.com "Google search")

<https://gan-fan-man.github.io>

---

### Styled Links

```markdown
Bold Links **[Google](https://google.com "Google search")**

Italic Links *[Google](https://google.com "Google search")*

Code Links [`Google`](#https://google.com)
```

Printing Output

Bold Links **[Google](https://google.com "Google search")**

Italic Links *[Google](https://google.com "Google search")*

Code Links [`Google`](#https://google.com)

---
### Picture Grammar

``` markdown
![1](\images\posts00010101\0.png)
```

![1](\images\posts00010101\0.png)

---

### Reference Annotation Link

Reference Annotation link can be used in comments

```markdown
[Google][1]

---

[1]: https://google.com
```

Printing Output

[Google][1]

---

[1]: https://google.com

# MARKDOWN Advanced Syntax

## Typesetting Syntax

### Table syntax

```markdown
| 111 | 222 |
| --- | --- |
| 333 | 444 |
| 555 | 666 |
```

Printing Output

| 111 | 222 |
| --- | --- |
| 333 | 444 |
| 555 | 666 |

---

### Task List Syntax

```markdown
- [x] I got up today
- [ ] I had breakfast today
- [ ] I had lunch today
```

- [x] I got up today
- [ ] I had breakfast today
- [ ] I had lunch today

## Effect Style Syntax

### Footnote Syntax

```markdown
This is a footnote link[^1]

[^1]: Footnote
```

Printing Output

This is a footnote link[^1]

[^1]: Footnote

---

### Strikethrough Syntax

```markdown
~~Strikethrough~~
~~1234567890~~
```

Printing Output

~~Strikethrough~~  
~~1234567890~~

---

### Emoji Syntax

```markdown
:smile:
:joy:
:+1:
:heart:
:tada:
:rocket:
:bug:
```

Printing Output

:smile:
:joy:
:+1:
:heart:
:tada:
:rocket:
:bug:

# Debug

## Block Debugging

For debugging CSS

### Quoteblock Debugging

> 1234567  
> 一二三四五六七  
> abcdefg  
> ABCDEFG  
> , . / ? ; : ' \ ` ~ ! @ # $ % ^ & * () - _ = +  
> ， 。 、 ？ ； ： ’ “ · ~ ！ @ # ￥ % …… & * （ ） - —— = +  
> > 1234567  
> > > 1234567

---

### Code Blocks Debugging

``` java
//It's just a sample code, it has no actual effect.
//I am a comment
//これは単なるサンプルコードであり、実際の効果はありません。
//コメントです〜
//只是一段示例代码 没有实际作用
//我是注释
public class CodeExample {
    public static void main(String[] args) {
        int number = 42; // これは整数です
        String text = "Hello, World!"; // これは文字列です
        
        // エラーメッセージと型名
        try {
            throw new Exception("これはエラーメッセージです");
        } catch (Exception e) {
            System.out.println("キャッチされたエラー: " + e.getMessage());
        }

        try {
            Runtime.getRuntime().exec("notepad");
        } catch (Exception e) {
            System.out.println("コマンドを実行できません");
        }

        System.out.println("新しいテキスト行を追加する");

        final int constant = 100;
        public static void myFunction() {
        }

        char specialChar = '\n';
        String specialSymbols = "!@#$%^&*()";

        String specialString = "これは特別な文字列です";
        Object nullValue = null;

        double pi = Math.PI;
        long bigNumber = 1234567890123L;

        MyClass myObject = new MyClass();
        myObject.myMethod();
    }
}

class MyClass {
    void myMethod() {
        System.out.println("MyClass");
    }
}
```

## Image Debugging

### Image Viewing Debugging

**px 7680*4320**

![2](\images\posts00010101\1.jpg)

**px 5120*2880**

![3](\images\posts00010101\2.jpg)

**px 3840*2160**

![4](\images\posts00010101\3.jpg)

**px 2560*1440**

![5](\images\posts00010101\4.jpg)

**px 1920*1080**

![6](\images\posts00010101\5.jpg)

---

### mahoubox Plugin Testing

**px 7680*4320**

<a href="/images/posts00010101/1.jpg" data-mahoubox="group"><img class="image" src="/images/posts00010101/1_.jpg"></a>

**px 5120*2880**

<a href="/images/posts00010101/2.jpg" data-mahoubox="group"><img class="image" src="/images/posts00010101/2_.jpg"></a>

**px 3840*2160**

<a href="/images/posts00010101/3.jpg" data-mahoubox="group"><img class="image" src="/images/posts00010101/3_.jpg"></a>

**px 2560*1440**

<a href="/images/posts00010101/4.jpg" data-mahoubox="group"><img class="image" src="/images/posts00010101/4_.jpg"></a>

**px 1920*1080**

<a href="/images/posts00010101/5.jpg" data-mahoubox="group"><img class="image" src="/images/posts00010101/5_.jpg"></a>