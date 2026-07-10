%global tl_name bold-extra
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Use bold small caps and typewriter fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bold-extra
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bold-extra.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bold-extra.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Allows access to 'extra' bold fonts for Computer Modern OT1 encoding
(the fonts are available in Metafont source). Since there is more than
one bold tt-family font set, the version required is selected by a
package option.

