Name:		texlive-bold-extra
Version:	0.1
Release:	1
Summary:	Use bold small caps and typewriter fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bold-extra
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bold-extra.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bold-extra.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Allows access to extra bold fonts for Computer Modern OT1
encoding (such fonts are available as MetaFont source). Since
there is more than one bold tt-family font set, the version
required is selected by a package option.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
