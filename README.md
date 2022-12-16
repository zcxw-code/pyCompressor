
**pyCompressor**
---
[![#](https://img.shields.io/badge/zcxw-zelenka.guru-%232BAD72)](https://zelenka.guru/members/2977610/)
[![#](https://img.shields.io/badge/zcxw-telegram-%23259cd8)](https://zcxw_lolz.t.me/)
=======
[![#](https://img.shields.io/github/downloads/zcxw-code/pyCompressor/total)](https://github.com/zcxw-code/pyCompressor/releases)
[![#](https://img.shields.io/github/license/zcxw-code/pyCompressor)](https://github.com/zcxw-code/pyCompressor/blob/main/LICENSE)
[![#](https://img.shields.io/github/stars/zcxw-code/pyCompressor)](#)
[![#](https://img.shields.io/github/forks/zcxw-code/pyCompressor)](https://github.com/zcxw-code/pyCompressor/fork)
___

## requirements

`pip3 install -r requirements.txt`
___
## usage
1. Place `pyCompressor.py` to the project folder
2. Create a `schema.json` in the project folder
3. Fill in the `schema.json`
    <pre><b>{</b>
        <font color="#00CD00">&quot;files&quot;</font>: <b>[</b><font color="#00CD00">&quot;./file.py&quot;</font>, <font color="#00CD00">&quot;./src/file.py&quot;</font><b>]</b>,
        <font color="#00CD00">&quot;dirs&quot;</font>: <b>[</b><font color="#00CD00">&quot;src&quot;</font><b>]</b>
    <b>}</b>
    </pre>
4. Run: `python pyCompressor.py`
    
___
## schema.json

* `files` = `list with project files in the sequence of importing local modules`
* `dirs` = `list with folders (local modules) of the project`
___
## example

`tree project_example`

<pre>
├── <font color="#0000FF"><b>local_modules</b></font>
│   ├── __init__.py
│   ├── module1.py
│   ├── module2.py
│   └── module3.py
│
└── main.py
</pre>

1. Place `pyCompressor.py` to the project folder and create `schema.json`
    <pre>
    ├── <font color="#0000FF">local_modules</b></font>
    │   ├── __init__.py
    │   ├── module1.py
    │   ├── module2.py
    │   ├── module3.py
    │   └── module3.py
    |
    ├── main.py
    ├── pyCompressor.py
    └── schema.json
    </pre>
2. Fill in the `schema.json`
    <pre><b>{</b>
        <font color="#00CD00">&quot;files&quot;</font>: <b>[</b>
            
            <font color="#00CD00">&quot;./local_modules/__init__.py&quot;</font>,
            <font color="#00CD00">&quot;./local_modules/module3.py&quot;</font>,
            <font color="#00CD00">&quot;./local_modules/module2.py&quot;</font>,
            <font color="#00CD00">&quot;./local_modules/module1.py&quot;</font>,
            <font color="#00CD00">&quot;./main.py&quot;</font>  
            
        <b>]</b>,
        <font color="#00CD00">&quot;dirs&quot;</font>: <b>[</b>
            <font color="#00CD00">&quot;local_modules&quot;</font>
        <b>]</b>
    <b>}</b>
    </pre>

3. Run: `python pyCompressor.py`
 
    `output`

    <pre>
    <font color="#00CD00">File </font><font color="#CD00CD">./local_modules/__init__.py</font><font color="#00CD00"> read.</font>
    <font color="#00CD00">File </font><font color="#CD00CD">./local_modules/module3.py</font><font color="#00CD00"> read.</font>
    <font color="#00CD00">File </font><font color="#CD00CD">./local_modules/module2.py</font><font color="#00CD00"> read.</font>
    <font color="#00CD00">File </font><font color="#CD00CD">./local_modules/module1.py</font><font color="#00CD00"> read.</font>
    <font color="#00CD00">File </font><font color="#CD00CD">./main.py</font><font color="#00CD00"> read.</font>
    <font color="#00CD00">Code fix.</font>
    <font color="#00CD00">Code minify.</font>
    <font color="#00CD00">Code compress.</font>
    <font color="#00CD00">Successfully! Files without compression: </font><font color="#00AA00"><b>968</b></font><font color="#008900"> bytes, and files compressed into a </font>
    <font color="#008900">single file: </font><font color="#00AA00"><b>376</b></font><font color="#008900"> bytes.</font>
    <font color="#00CD00">Code save. To </font>
    </pre>
4. Test `python ./example_compress/output.py`

    `output`

    ```
    Starting module1 functions
    module1:func1
    module1:func1
    module1:func1
    Starting module2 functions
    module2:func1
    module2:func2
    module2:func3
    Starting module3 functions
    module3:func1
    module3:func2
    module3:func3
    ```
___

## Important

> There should be no functions and classes of the same name in the project.
___