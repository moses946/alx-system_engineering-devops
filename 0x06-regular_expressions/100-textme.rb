#!/usr/bin/env ruby
result =  ARGV[0].scan(/from:(\+?[\w]+)\] \[to:(\+?[\w]+)\] \[flags:([-:\d]+)\]/).join
puts result ? "#{$1},#{$2},#{$3}" : ""
