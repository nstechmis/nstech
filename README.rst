========
如何開發
========

本網站利用 `pelican <http://blog.getpelican.com/>`_ (利用Python所寫成的static site generator)開發.開發環境是Ubuntu 14.10.


第一次的安裝設定
----------------

1. 安裝 `git <http://git-scm.com/>`_, `pip <https://pypi.python.org/pypi/pip>`_ 及 `virtualenv <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_ :

.. code-block:: bash

    $ sudo apt-get install git
    $ sudo apt-get install python-pip
    $ sudo pip install virtualenv

2. 進入Python虛擬環境:

.. code-block:: bash

    $ cd
    $ mkdir dev
    $ virtualenv ~/dev/nstechdev/
    $ cd ~/dev/nstechdev/
    $ source bin/activate

3. 利用git clone原始碼:

.. code-block:: bash

    $ cd ~/dev/nstechdev/
    $ git clone https://github.com/nstechmis/nstech.git

4. 安裝必要工具:

.. code-block:: bash

    $ cd ~/dev/nstechdev/nstech
    $ sudo pip install -r requirements.txt

5. 安裝pelican的 `i18n_subsites <https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites>`_ plugin:

    下載 ``i18n_subsites`` 目錄並放到 ``~/dev/nstechdev/nstech/plugins`` 目錄下

.. code-block:: bash

    $ make download

6. 產生CSS檔:

.. code-block:: bash

    $ make scss


日常開發
--------

.. code-block:: bash

    $ cd ~/dev/nstechdev/
    $ source bin/activate
    $ cd nstech
    # if scss file changes
    $ make html
    # start edit and develope

上傳
----

.. code-block:: bash

    $ make clean
    $ make publish
    $ make github_upload

參考
----

`Online reStructuredText editor <http://rst.ninjs.org/>`_

`Can I use an image to trigger a modal window in Bootstrap? <http://stackoverflow.com/questions/15423532/can-i-use-an-image-to-trigger-a-modal-window-in-bootstrap>`_

`Bootstrap Image trigger modal example code <http://www.bootply.com/7wOLkC9AVX>`_

`iHover <http://gudh.github.io/ihover/dist/>`_ (`src <https://github.com/gudh/ihover>`_)

`bootstrap image hover overlay with icon <http://stackoverflow.com/questions/26823237/bootstrap-image-hover-overlay-with-icon>`_
