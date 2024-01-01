#! /usr/bin/tclsh 
# Generated for VCF on 2024-01-01 17:50:16.150341
# This task is used to run Formal Verification on the design.

set_app_mode FPV

set_app_var a true
set_app_var b true

set_blackbox -designs { add.v sub.v }
set_blackbox -cells { add.v sub.v }

report_blackbox

read_file -top adder -format verilog -sva -vcs "-f { adder.v adder_tb.v mult.v }" -assert svaext -lca

set_clock -name clk -period 10

check_fv block

