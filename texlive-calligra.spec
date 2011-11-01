Name:		texlive-calligra
Version:	20100503
Release:	1
Summary:	Calligraphic font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/calligra
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calligra.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/calligra.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A calligraphic font in the handwriting style of the author,
Peter Vanroose. The font is supplied as MetaFont source LaTeX
support of the font is provided in the calligra package in the
fundus bundle.

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
%{_texmfdistdir}/fonts/source/public/calligra/callig15.mf
%{_texmfdistdir}/fonts/source/public/calligra/calligra.mf
%{_texmfdistdir}/fonts/tfm/public/calligra/callig15.tfm
%doc %{_texmfdistdir}/doc/latex/calligra/README
%doc %{_texmfdistdir}/doc/latex/calligra/testfont.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
