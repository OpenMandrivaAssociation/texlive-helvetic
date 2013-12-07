# revision 31835
# category Package
# catalog-ctan /fonts/urw/base35
# catalog-date 2012-06-06 22:57:48 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-helvetic
Version:	20120606
Release:	5
Summary:	URW "Base 35" font pack for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urw/base35
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/helvetic.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: - Century Schoolbook (substituting for
Adobe's New Century Schoolbook); - Dingbats (substituting for
Adobe's Zapf Dingbats); - Nimbus Mono L (substituting for
Abobe's Courier); - Nimbus Roman No9 L (substituting for
Adobe's Times); - Nimbus Sans L (substituting for Adobe's
Helvetica); - Standard Symbols L (substituting for Adobe's
Symbol); - URW Bookman; - URW Chancery L Medium Italic
(substituting for Adobe's Zapf Chancery); - URW Gothic L Book
(substituting for Adobe's Avant Garde); and - URW Palladio L
(substituting for Adobe's Palatino).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/helvetic/config.uhv
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvb8a.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvb8an.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvbo8a.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvbo8an.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvr8a.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvr8an.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvro8a.afm
%{_texmfdistdir}/fonts/afm/adobe/helvetic/phvro8an.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvb8a.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvb8ac.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvbo8a.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvbo8ac.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvr8a.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvr8ac.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvro8a.afm
%{_texmfdistdir}/fonts/afm/urw/helvetic/uhvro8ac.afm
%{_texmfdistdir}/fonts/map/dvips/helvetic/uhv.map
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb7tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb8cn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb8rn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvb8tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbc7tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbc8tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo7tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo8cn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo8rn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbo8tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbon.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvbrn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr7tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr8cn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr8rn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvr8tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvrc.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvrc7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvrc7tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvrc8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvrc8tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro7t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro7tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro8c.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro8cn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro8r.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro8rn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro8t.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvro8tn.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvron.tfm
%{_texmfdistdir}/fonts/tfm/adobe/helvetic/phvrrn.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arb10u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arb2n.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arb7j.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arb8u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arb9t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/ari10u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/ari2n.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/ari7j.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/ari8u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/ari9t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arj10u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arj2n.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arj7j.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arj8u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arj9t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arr10u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arr2n.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arr7j.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arr8u.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/arr9t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvb.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvb8t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvbi.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvbi8t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvr.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvr8t.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvri.tfm
%{_texmfdistdir}/fonts/tfm/monotype/helvetic/mhvri8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb8cn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb8rn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvb8tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbc7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbc8tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbi7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbi8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbi8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbi8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo8cn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo8rn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvbo8tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr8cn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr8rn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvr8tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvrc7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvrc7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvrc8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvrc8tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri8cn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri8rn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvri8tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro7t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro7tn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro8c.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro8cn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro8r.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro8rn.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro8t.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/helvetic/uhvro8tn.tfm
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvb8a.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvb8a.pfm
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvb8ac.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvb8ac.pfm
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvbo8a.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvbo8a.pfm
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvbo8ac.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvbo8ac.pfm
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvr8a-105.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvr8a.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvr8a.pfm
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvr8ac.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvr8ac.pfm
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvro8a-105.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvro8a.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvro8a.pfm
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvro8ac.pfb
%{_texmfdistdir}/fonts/type1/urw/helvetic/uhvro8ac.pfm
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb7t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb7tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb8c.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb8cn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb8t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvb8tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbc.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbc7tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbc8tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo7t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo7tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo8c.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo8cn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo8t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbo8tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbon.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvbrn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr7t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr7tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr8c.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr8cn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr8t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvr8tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvrc.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvrc7t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvrc7tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvrc8t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvrc8tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro7t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro7tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro8c.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro8cn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro8t.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvro8tn.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvron.vf
%{_texmfdistdir}/fonts/vf/adobe/helvetic/phvrrn.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvb.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvb8t.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvbi.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvbi8t.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvr.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvr8t.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvri.vf
%{_texmfdistdir}/fonts/vf/monotype/helvetic/mhvri8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvb7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvb7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvb8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvb8cn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvb8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvb8tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbc7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbc8tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbi7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbi8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbi8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbo7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbo7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbo8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbo8cn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbo8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvbo8tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvr7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvr7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvr8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvr8cn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvr8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvr8tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvrc7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvrc7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvrc8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvrc8tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvri7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvri7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvri8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvri8cn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvri8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvri8tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvro7t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvro7tn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvro8c.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvro8cn.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvro8t.vf
%{_texmfdistdir}/fonts/vf/urw35vf/helvetic/uhvro8tn.vf
%{_texmfdistdir}/tex/latex/helvetic/8ruhv.fd
%{_texmfdistdir}/tex/latex/helvetic/omluhv.fd
%{_texmfdistdir}/tex/latex/helvetic/omsuhv.fd
%{_texmfdistdir}/tex/latex/helvetic/ot1uhv.fd
%{_texmfdistdir}/tex/latex/helvetic/t1uhv.fd
%{_texmfdistdir}/tex/latex/helvetic/ts1uhv.fd

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex %{buildroot}%{_texmfdistdir}
