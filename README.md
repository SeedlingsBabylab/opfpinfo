# opfpinfo

This script produces a table containing the personal info status of all the subjects and visits for video files.
It also indicated whether the given opf file passes all the formatting checks


## usage

```
$ python opfpinfo.py [all_opf_files_dir] [all_personal_info_files_dir] [passed_check_file.csv]
```

This script should be used in conjunction with the gatheropffiles script and a few datavyu scripts.
The gatheropffiles script will crawl the Subject_Files directory tree and accumulate all the opf files
into a specified directory. You should then pass the path of that directory (with all the opf files found
  by gatheropffiles) to the batch_run_all.rb and batch_personalinfo.rb script contained in datavyu_scripts.
