#! /usr/bin/tclsh 
# Generated on 2023-12-20 14:43:23.398359
# This task is used to run Formal Verification on the design.

set_app_mode FPV

set_blackbox -designs { add.v sub.v }
set_blackbox -cells { add0 sub0 }
read_file -top adder -format verilog -sva -vcs "-f { adder.v adder_tb.v mult.v }" -assert svaext -lca

create_clock -name clk -period 10

create_reset -name rst -sense high

sim_run -stable 
sim_save_reset 

check_fv block

