# revision 16433
# category Package
# catalog-ctan /support/latexdiff
# catalog-date 2009-12-14 16:43:49 +0100
# catalog-license gpl
# catalog-version 0.5
Name:		texlive-latexdiff
Version:	0.5
Release:	2
Summary:	Determine and mark up significant differences between latex files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/latexdiff
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexdiff.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latexdiff.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-latexdiff.bin = %{EVRD}
%rename latexdiff

%description
Latexdiff is a Perl script for visual mark up and revision of
significant differences between two latex files. Various
options are available for visual markup using standard latex
packages such as color. Changes not directly affecting visible
text, for example in formatting commands, are still marked in
the latex source. A rudimentary revision facilility is provided
by another Perl script, latexrevise, which accepts or rejects
all changes. Manual editing of the difference file can be used
to override this default behaviour and accept or reject
selected changes only.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/latexdiff-vc
%{_bindir}/latexdiff
%{_bindir}/latexrevise
%{_texmfdistdir}/scripts/latexdiff/latexdiff-vc.pl
%{_texmfdistdir}/scripts/latexdiff/latexdiff.pl
%{_texmfdistdir}/scripts/latexdiff/latexrevise.pl
%doc %{_texmfdistdir}/doc/latex/latexdiff/CHANGES
%doc %{_texmfdistdir}/doc/latex/latexdiff/LICENSE
%doc %{_texmfdistdir}/doc/latex/latexdiff/Makefile
%doc %{_texmfdistdir}/doc/latex/latexdiff/README
%doc %{_texmfdistdir}/doc/latex/latexdiff/contrib/latexdiff-wrap
%doc %{_texmfdistdir}/doc/latex/latexdiff/contrib/latexdiff.spec
%doc %{_texmfdistdir}/doc/latex/latexdiff/example/example-draft.tex
%doc %{_texmfdistdir}/doc/latex/latexdiff/example/example-rev.tex
%doc %{_texmfdistdir}/doc/latex/latexdiff/latexdiff
%doc %{_texmfdistdir}/doc/latex/latexdiff/latexdiff-fast
%doc %{_texmfdistdir}/doc/latex/latexdiff/latexdiff-man.pdf
%doc %{_mandir}/man1/latexdiff-vc.1*
%doc %{_texmfdir}/doc/man/man1/latexdiff-vc.man1.pdf
%doc %{_mandir}/man1/latexdiff.1*
%doc %{_texmfdir}/doc/man/man1/latexdiff.man1.pdf
%doc %{_mandir}/man1/latexrevise.1*
%doc %{_texmfdir}/doc/man/man1/latexrevise.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/latexdiff/latexdiff-vc.pl latexdiff-vc
    ln -sf %{_texmfdistdir}/scripts/latexdiff/latexdiff.pl latexdiff
    ln -sf %{_texmfdistdir}/scripts/latexdiff/latexrevise.pl latexrevise
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
