Name:		texlive-bold-extra
Version:	17076
Release:	1
Summary:	Use bold small caps and typewriter fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bold-extra
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bold-extra.r17076.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bold-extra.doc.r17076.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Allows access to extra bold fonts for Computer Modern OT1
encoding (such fonts are available as MetaFont source). Since
there is more than one bold tt-family font set, the version
required is selected by a package option.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bold-extra/bold-extra.sty
%doc %{_texmfdistdir}/doc/latex/bold-extra/bold-extra.pdf
%doc %{_texmfdistdir}/doc/latex/bold-extra/bold-extra.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
