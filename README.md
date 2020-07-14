**Start**

1. Translate

    You can get help.
    ```shell
    python main.py translate -h
    ```
   
    Output
    ```shell
    [2020-06-09 14:08:19]  translate: -d <database>
        -t <table>
        -p <password>
        -u <username>
        -s <src_column>
        -a <dest_column> 
        -sl <src_lan> 
        -dl <dest_lan>
        -c <condition_column>
    ```

    Run translate.
    ```shell
    python main.py translate -d fungame -t games -p root -u postgres -s name -a name_sk -sl en -dl sk -c id
    python main.py translate -d body_build_at -t video_data -p wyysdsa! -u cpx -s video_name -a video_name -sl en -dl de -c video_id
    ```
   