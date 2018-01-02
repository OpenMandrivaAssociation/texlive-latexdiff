Name:		texlive-latexdiff
Version:	1.2.1
Release:	1
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
%{_texmfdistdir}/scripts/latexdiff
%doc %{_mandir}/man1/latexdiff-vc.1*
%doc %{_texmfdistdir}/doc/man/man1/latexdiff-vc.man1.pdf
%doc %{_mandir}/man1/latexdiff.1*
%doc %{_texmfdistdir}/doc/man/man1/latexdiff.man1.pdf
%doc %{_mandir}/man1/latexrevise.1*
%doc %{_texmfdistdir}/doc/man/man1/latexrevise.man1.pdf
%doc %{_texmfdistdir}/doc/support/latexdiff

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
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
