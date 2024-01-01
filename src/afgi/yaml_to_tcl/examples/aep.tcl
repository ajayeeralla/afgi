#! /usr/bin/tclsh 
# Generated for VCF on 2024-01-01 17:50:36.849453
# Generate AEP for the design.

set_app_mode AEP

set_app_var a true
set_app_var b true

set_blackbox -designs { add.v sub.v }
set_blackbox -cells { add.v sub.v }

report_blackbox

read_file -top adder -aep fsm_sss+b+c+d -cov fsm_state+fsm_trans -format verilog -sva -vcs "-f { adder.v adder_tb.v mult.v }" -assert svaext -lca

set_clock -name clk -period 10

check_fv block

