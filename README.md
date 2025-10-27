# Render publications

1. xls file in data with columns: Title, Authors, PID

2. convert to csv 

```bash
python code/xls2csv_with_urls.py data/publications.xlsx data/publications.csv
```

3. convert csv to markdown

```bash
python code/make_publications.py < data/publications.csv >  publications.md
 ```

# Render events

1. xls file in data with columsn: Type, Description, Audience, Year, Outcome

2. convert to csv 

```bash
python code/xls2csv_with_urls.py data/events.xlsx data/events.csv
```

3. convert csv to markdown

```bash
python code/make_events.py < data/events.csv > events.md
```
