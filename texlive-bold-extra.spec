# revision 17076
# category Package
# catalog-ctan /macros/latex/contrib/bold-extra
# catalog-date 2010-02-23 16:09:16 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-bold-extra
Version:	0.1
Release:	4
Summary:	Use bold small caps and typewriter fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bold-extra
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bold-extra.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bold-extra.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 749797
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 717961
- texlive-bold-extra
- texlive-bold-extra
- texlive-bold-extra
- texlive-bold-extra
- texlive-bold-extra

