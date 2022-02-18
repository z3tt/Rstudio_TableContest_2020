<h1 style="font-weight:normal" align="center">
  &nbsp;What do I binge next?<br>An overview of the Best IMDb TV shows&nbsp;
</h1>

<div align="center">

&nbsp;&nbsp;&nbsp;
<a href="https://www.cedricscherer.com"><img border="0" alt="Blog" src="https://assets.dryicons.com/uploads/icon/svg/4926/home.svg" width="35" height="35"></a>&nbsp;&nbsp;&nbsp;
<a href="mailto:info@data-vizard.com"><img border="0" alt="Email" src="https://assets.dryicons.com/uploads/icon/svg/8009/02dc3a5c-6504-4347-85fb-3f510cfecc45.svg" width="35" height="35"></a>&nbsp;&nbsp;&nbsp;
<a href="https://twitter.com/CedScherer"><img border="0" alt="Twitter" src="https://assets.dryicons.com/uploads/icon/svg/8385/c23f7ffc-ca8d-4246-8978-ce9f6d5bcc99.svg" width="35" height="35"></a>&nbsp;&nbsp;&nbsp; 
<a href="https://www.instagram.com/cedscherer/"><img border="0" alt="Instagram" src="https://assets.dryicons.com/uploads/icon/svg/8330/62263227-bb78-4b42-a9a9-e222e0cc7b97.svg" width="35" height="35"></a>&nbsp;&nbsp;&nbsp;
<a href="https://www.behance.net/cedscherer"><img border="0" alt="Behance" src="https://assets.dryicons.com/uploads/icon/svg/8264/04073ce3-5b98-4f32-88d3-82b2ef828066.svg" width="35" height="35"></a>&nbsp;&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/cedricpscherer/"><img border="0" alt="LinkedIn" src="https://assets.dryicons.com/uploads/icon/svg/8337/a347cd89-1662-4421-be90-58e5e8004eae.svg" width="35" height="35"></a>&nbsp;&nbsp;&nbsp;
<a href="https://www.buymeacoffee.com/z3tt"><img border="0" alt="BuyMeACoffee" src="https://www.buymeacoffee.com/assets/img/guidelines/logo-mark-3.svg" width="35" height="35"></a>&nbsp;&nbsp;&nbsp;

</div>

The table shows relevant details of the top 250 TV shows as rated by IMDb users. I focussed on displaying the details I and my friends care about: of course the ranking and overall rating but additionally the runtime per episode, genres, number of seasons and episodes, ID of the best episodes. But most importantly—the trend of ratings as the TV show progresses.

_**[The table was highlighted as "honorable mention" by the jury](https://blog.rstudio.com/2020/12/23/winners-of-the-2020-rstudio-table-contest/) 🎉**_

## Top 250:

<details>
  <summary>Expand to see the loooong version</summary>
  <img src="./output/IMDb_Top250.png"/>
</details>

## Documentaries only:
![](./output/IMDb_TopDocumentary.png)

### Other Versions by Rank:

<details>
  <summary>Top 50</summary>
  <img src="./output/IMDb_Top50.png"/>
</details>

<details>
  <summary>Top 100</summary>
  <img src="./output/IMDb_Top100.png"/>
</details>

### Other Versions by Genres:

<details>
  <summary>Animation</summary>
  <img src="./output/IMDb_TopAnimation.png"/>
</details>

<details>
  <summary>Comedy</summary>
  <img src="./output/IMDb_TopComedy.png"/>
</details>

<details>
  <summary>Drama</summary>
  <img src="./output/IMDb_TopDramay.png"/>
</details>

<details>
  <summary>Action</summary>
  <img src="./output/IMDb_TopAction.png"/>
</details>

## Packages used:

`gt`, `reticulate`, `dplyr`, `tidyr`, `readr`, `magrittr`, `here`, `glue`, `pkgconfig`

## Details:

**Visualizations:** To visualize the runtime I decided to use a restrained, grey-toned, area-scaled circle. The normalized trends in episode ratings are visualized as stripes similar to the famous ["warming stripes" by Ed Hawkins](https://en.wikipedia.org/wiki/Warming_stripes). In addition, a line indicates the average rating per season on a range from 1 to 10.

**Data:** The data is a mixture of scraped data using a modified [Python script](https://github.com/WittmannF/imdb-tv-ratings/blob/master/IMDB_get_ratings.ipynb) (ranks, ratings, votes, year) and data downloaded from the [IMDb dataset interface](https://www.imdb.com/interfaces/) (title basics: original title, genre, runtime). The data was cleaned (e.g. correct wrong runtimes, title spellings etc) and missing entries filled. (However, some series are returned as having 1 season only but have several actually and I didn't find a good workaround yet.)

***

<div align="center">
  <h4>Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</h4>
<div style="width:300px; height:200px">
<img src=https://camo.githubusercontent.com/00f7814990f36f84c5ea74cba887385d8a2f36be/68747470733a2f2f646f63732e636c6f7564706f7373652e636f6d2f696d616765732f63632d62792d6e632d73612e706e67 alt="" height="42">
</div>
  <br>
  <a href="https://www.buymeacoffee.com/z3tt" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-1.svg" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
  <br><br>
</div>

