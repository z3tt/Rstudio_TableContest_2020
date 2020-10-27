
# What do I binge next? An overview of the Best IMDb TV shows

![](./output/IMDb_Top100.png)

### Packages used:

`gt`, `reticulate`, `dplyr`, `tidyr`, `readr`, `magrittr`, `here`, `glue`, `pkgconfig`

### Short Description:

The table shows relevant details of the top 250 TV shows as rated by IMDb users. I focussed on displaying the details I and my friends care about: of course the ranking and overall rating but additionally the runtime per episode, genres, number of seasons and episodes, ID of the best episodes. But most importantly—the trend of ratings as the TV show progresses.

To visualize the runtime I decided to use a restrained, grey-toned, area-scaled circle. The normalized trends in episode ratings are visualized as stripes similar to the famous "warming stripes" by Ed Hawkins. In addition, a line indicates the average rating per season on a range from 1 to 10.

### Long Description:

The table shows relevant details of the top 250 TV shows as rated by IMDb users. I focussed on displaying the details I and my friends care about: of course the ranking and overall rating but additionally the runtime per episode, genres, number of seasons and episodes, ID of the best episodes. But most importantly—the trend of ratings as the TV show progresses.

**Visualizations:** To visualize the runtime I decided to use a restrained, grey-toned, area-scaled circle. The normalized trends in episode ratings are visualized as stripes similar to the famous ["warming stripes" by Ed Hawkins](https://en.wikipedia.org/wiki/Warming_stripes). In addition, a line indicates the average rating per season on a range from 1 to 10.

**Data:** The data is a mixture of scraped data using a modified [Python script](https://github.com/WittmannF/imdb-tv-ratings/blob/master/IMDB_get_ratings.ipynb) (ranks, ratings, votes, year) and data downloaded from the [IMDb dataset interface](https://www.imdb.com/interfaces/) (title basics: original title, genre, runtime). The data was cleaned (e.g. correct wrong runtimes, title spellings etc) and missing entries filled. (However, some series are returned as having 1 season only but have several actually and I didn't find a good workaround yet.)
