# This file is automatically generated.  DO NOT EDIT!
# Generated from: 	NetBSD: mknative-gcc,v 1.68 2012/09/25 06:55:10 skrll Exp 
# Generated from: NetBSD: mknative.common,v 1.9 2007/02/05 18:26:01 apb Exp 
#
# This spec file is read by gcc when linking.  It is used to specify the
# standard libraries we need in order to link with -fopenmp.
*link_gomp: -lgomp %{static: -lintl}