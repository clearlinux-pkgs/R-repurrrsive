#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-repurrrsive
Version  : 1.0.0
Release  : 8
URL      : https://cran.r-project.org/src/contrib/repurrrsive_1.0.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/repurrrsive_1.0.0.tar.gz
Summary  : Examples of Recursive Lists and Nested or Split Data Frames
Group    : Development/Tools
License  : CC0-1.0
Requires: R-tibble
BuildRequires : R-tibble
BuildRequires : buildreq-R

%description
and 'XML', for use in teaching and examples. Examples include color
    palettes, Game of Thrones characters, 'GitHub' users and repositories,
    music collections, and entities from the Star Wars universe. Data from
    the 'gapminder' package is also included, as a simple data frame and
    in nested and split forms.

%prep
%setup -q -c -n repurrrsive
cd %{_builddir}/repurrrsive

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1616434886

%install
export SOURCE_DATE_EPOCH=1616434886
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library repurrrsive
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library repurrrsive
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library repurrrsive
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc repurrrsive || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/repurrrsive/DESCRIPTION
/usr/lib64/R/library/repurrrsive/INDEX
/usr/lib64/R/library/repurrrsive/Meta/Rd.rds
/usr/lib64/R/library/repurrrsive/Meta/data.rds
/usr/lib64/R/library/repurrrsive/Meta/features.rds
/usr/lib64/R/library/repurrrsive/Meta/hsearch.rds
/usr/lib64/R/library/repurrrsive/Meta/links.rds
/usr/lib64/R/library/repurrrsive/Meta/nsInfo.rds
/usr/lib64/R/library/repurrrsive/Meta/package.rds
/usr/lib64/R/library/repurrrsive/NAMESPACE
/usr/lib64/R/library/repurrrsive/NEWS.md
/usr/lib64/R/library/repurrrsive/R/repurrrsive
/usr/lib64/R/library/repurrrsive/R/repurrrsive.rdb
/usr/lib64/R/library/repurrrsive/R/repurrrsive.rdx
/usr/lib64/R/library/repurrrsive/data/Rdata.rdb
/usr/lib64/R/library/repurrrsive/data/Rdata.rds
/usr/lib64/R/library/repurrrsive/data/Rdata.rdx
/usr/lib64/R/library/repurrrsive/extdata/discog.json
/usr/lib64/R/library/repurrrsive/extdata/gh_repos.json
/usr/lib64/R/library/repurrrsive/extdata/gh_repos.xml
/usr/lib64/R/library/repurrrsive/extdata/gh_users.json
/usr/lib64/R/library/repurrrsive/extdata/gh_users.xml
/usr/lib64/R/library/repurrrsive/extdata/got_chars.json
/usr/lib64/R/library/repurrrsive/extdata/got_chars.xml
/usr/lib64/R/library/repurrrsive/extdata/wesanderson.json
/usr/lib64/R/library/repurrrsive/extdata/wesanderson.xml
/usr/lib64/R/library/repurrrsive/help/AnIndex
/usr/lib64/R/library/repurrrsive/help/aliases.rds
/usr/lib64/R/library/repurrrsive/help/figures/wesanderson-rstudio-view.png
/usr/lib64/R/library/repurrrsive/help/paths.rds
/usr/lib64/R/library/repurrrsive/help/repurrrsive.rdb
/usr/lib64/R/library/repurrrsive/help/repurrrsive.rdx
/usr/lib64/R/library/repurrrsive/html/00Index.html
/usr/lib64/R/library/repurrrsive/html/R.css
/usr/lib64/R/library/repurrrsive/tests/testthat.R
/usr/lib64/R/library/repurrrsive/tests/testthat/helper.R
/usr/lib64/R/library/repurrrsive/tests/testthat/reference/discog.rds
/usr/lib64/R/library/repurrrsive/tests/testthat/reference/gh_repos.rds
/usr/lib64/R/library/repurrrsive/tests/testthat/reference/gh_users.rds
/usr/lib64/R/library/repurrrsive/tests/testthat/reference/got_chars.rds
/usr/lib64/R/library/repurrrsive/tests/testthat/reference/sw_films.rds
/usr/lib64/R/library/repurrrsive/tests/testthat/reference/sw_people.rds
/usr/lib64/R/library/repurrrsive/tests/testthat/reference/sw_planets.rds
/usr/lib64/R/library/repurrrsive/tests/testthat/reference/sw_species.rds
/usr/lib64/R/library/repurrrsive/tests/testthat/reference/sw_starships.rds
/usr/lib64/R/library/repurrrsive/tests/testthat/reference/sw_vehicles.rds
/usr/lib64/R/library/repurrrsive/tests/testthat/reference/wesanderson.rds
/usr/lib64/R/library/repurrrsive/tests/testthat/test-discog.R
/usr/lib64/R/library/repurrrsive/tests/testthat/test-gh_users_repos.R
/usr/lib64/R/library/repurrrsive/tests/testthat/test-got_chars.R
/usr/lib64/R/library/repurrrsive/tests/testthat/test-swapi.R
/usr/lib64/R/library/repurrrsive/tests/testthat/test-wesanderson.R
