# Sea water temperature and light intensity at high-Arctic subtidal shallows – 16 years perspective
This repository contains Python code to (i) create CF-NetCDF (.nc) files from .csv, and (ii) minimally process long-term data (e.g., annual and monthly means).

## Requirements
1. Software: [Anaconda](https://www.anaconda.com/download) (Spyder, the Scientific Python Development Environment, is a free integrated development environment (IDE) that is included with Anaconda).
2. Datasets: Datasets and their metadata have been deposited in stable IO PAN Geonetwork repository, downloadable via OPeNDAP:
   
   - [S1s](http://geo.iopan.pl/geonetwork/srv/eng/catalog.search#/metadata/7bbe99ea-1c00-446d-af4e-d76b0d510730) (8m)
   - [S1d](http://geo.iopan.pl/geonetwork/srv/eng/catalog.search#/metadata/b0901d4d-86b1-467a-b2a2-ff10bb9478a5) (13m)
   - [S2s](http://geo.iopan.pl/geonetwork/srv/eng/catalog.search#/metadata/caabcd76-2850-4c26-a3a9-dc510f3ed398) (7m)
   - [S2d](http://geo.iopan.pl/geonetwork/srv/eng/catalog.search#/metadata/13ade6a5-2118-422b-ba91-0c19ca098e65) (15m)

    *The above-mentioned .nc files together with processed .csv (e.g, monthly and annual means, derived from this code) are also available via [Figshare](https://doi.org/10.6084/m9.figshare.21881460)


## Description

As part of an ecological monitoring initiative, the **Institute of Oceanology Polish Academy of Sciences IOPAN** (Marine Ecology Department) deployed a series of bespoke metal constructions to conduct a long-term multipurpose experiment assessing the ecology of hard-bottom assemblages in the shallow subtidal of southern Isfjorden proper between 2006 and 2022 (16yr). Attached to these submerged constructions were data-loggers of temperature and light intensity. Two stations (S1 and S2) and two depth strata (shallow infralittoral [s], and circalittoral [d]) were considered for the deployments.

Further details about logger deployment and study site overall can be found in the data descriptor:

  **[Moreno B](https://orcid.org/0000-0002-9751-6307)**, Sowa A, Reginia K, Balazy P, Chelchowski M, Ronowicz M, Kuklinski P (2024) Sea water temperature and light intensity at high-Arctic subtidal shallows – 16 years perspective. *Scientific Data*, [doi](____)]

## Additional resources
Additionally, a series of useful links of the conventions/standards/tools, and other resources used:

| Acronym| Resource title | type | version | link |
| -------| -------------- | ---- | ------- | ----- |
| ACDD | Attribute Convention for dataset Discovery | convention - discovery metadata | v. 1.3 | [ACDD documentation](https://adc.met.no/node/4)|
| CF | Climate and forecast metadata convention | convention - use metadata | v. 1.10 |[CF Convention](https://cfconventions.org/index.html)|
| CF | Climate and forecast metadata convention | standard names| v. 83 | [CF standard names](https://cfconventions.org/Data/cf-standard-names/current/src/cf-standard-name-table.xml)|
| eCUDO.pl | Oceanographic Data and Information System | data infrastructure project (Poland)| | [eCUDO.pl](https://odis.ecudo.pl/)|
| GCMD | Global Change Master Directory | keywords | v. 17.1 | [GCMD keywords](https://gcmd.earthdata.nasa.gov/KeywordViewer/)|
| IOPAN GeoNet | Geonetwork of the Institute of Oceanology Polish Academy of Sciences| ocean data repository| | [IO PAN Geonetwork](https://geo.iopan.pl/geonetwork/srv/eng/catalog.search#/home)|
| NetCDF | Network Common Data Form | standard | | [NetCDF](https://www.unidata.ucar.edu/software/netcdf/)|
| NorDataNet | Norwegian Scientific Data Network - Nansen Legacy | template generator   | | [NorDataNet](https://www.nordatanet.no/aen/template-generator/config%3DCF-NetCDF)|
| OPeNDAP | Open-source Project for a Network Data Access Protocol | community standard   | | [OPeNDAP](https://www.opendap.org/)|
| SIOS | Svalbard Integrated Arctic Earth Observing System | data management tools| | [SIOS tools](https://sios-svalbard.org/DMtools)|


Further resources can be found in [Luke Marsden GitHub](https://github.com/lhmarsden/NetCDF-CF_workshops), Data Manager of The Nansen Legacy.

## References 

- **[Moreno B](https://orcid.org/0000-0002-9751-6307)**, Sowa A, Reginia K, Balazy P, Chelchowski M, Ronowicz M, Kuklinski P (2024) Sea water temperature and light intensity at high-Arctic subtidal shallows – 16 years perspective. *Scientific Data*, [doi](____)]
- Moreno, B., Sowa, A., Ronowicz, M. & Kuklinski, P. Sea water temperature and light intensity at hard-bottom high-Arctic shallow subtidal fjord locations. [Figshare](https://doi.org/10.6084/m9.figshare.21881460) (2023).
- Moreno, B. Sea water temperature and light intensity at sea floor data (2006–2022) at station **[S1, 8m (S1s)](http://geo.iopan.pl/geonetwork/srv/eng/catalog.search#/metadata/7bbe99ea-1c00-446d-af4e-d76b0d510730)**, Isfjorden (78°N). IO PAN Geonetwork (2023).
- Moreno, B. Sea water temperature and light intensity at sea floor data (2006–2022) at station **[S1, 13m (S1d)](http://geo.iopan.pl/geonetwork/srv/eng/catalog.search#/metadata/b0901d4d-86b1-467a-b2a2-ff10bb9478a5)**, Isfjorden (78°N). IO PAN Geonetwork (2023).
- Moreno, B. Sea water temperature and light intensity at sea floor data (2006–2022) at station **[S2, 7m (S2s)](http://geo.iopan.pl/geonetwork/srv/eng/catalog.search#/metadata/caabcd76-2850-4c26-a3a9-dc510f3ed398)**, Isfjorden (78°N). IO PAN Geonetwork (2023).
- Moreno, B. Sea water temperature and light intensity at sea floor data (2006–2022) at station **[S2, 15m (S2d)](http://geo.iopan.pl/geonetwork/srv/eng/catalog.search#/metadata/13ade6a5-2118-422b-ba91-0c19ca098e65)**, Isfjorden (78°N). IO PAN Geonetwork (2023)
