#!/usr/bin/env ruby

require 'openssl'
require 'io/console'
$stdout.sync = true

FLAG = ENV['FLAG'] || 'MetaCTF{test_flag}'


def encrypt(msg, key)
  cipher = OpenSSL::Cipher.new('AES-128-CBC')
  # key.each_byte do |byte|
  #   puts byte.to_s(2).rjust(8, '0')
  # end
  # puts msg.inspect
  cipher.encrypt
  iv = cipher.random_iv
  # iv = "\x20" * 16
  # iv = ";\xB2*\x06Iz\x19 r\xB9H\xC8\x01\x1E\xEE\x0E"
  # iv = "\x3b\xb2\x2a\x06\x49\x7a\x19\x20\x72\xb9\x48\xc8\x01\x1e\xee\x0e"
  # cipher.iv = iv
  puts "iv: #{iv.inspect}"
  puts "len(iv): #{iv.length}"
  cipher.key = key
  encrypted = cipher.update(msg) + cipher.final
  puts "encrypted: #{encrypted.inspect}"
  puts "len(encrypted): #{encrypted.length}"
  iv + encrypted
end

def decrypt(ct, key)
  decipher = OpenSSL::Cipher.new('AES-128-CBC')
  decipher.decrypt
  decipher.key = key
  iv = ct[0..15]
  # iv = "\x00" * 16
  encrypted_msg = ct[16..-1]
  decipher.iv = iv
  # puts iv.inspect
  decipher.update(encrypted_msg) + decipher.final
end

def main
  key = OpenSSL::Cipher.new('AES-128-CBC').random_key
  # key = 'this is the keyi'

  while true
    puts '1. Request print command'
    puts '2. Execute print command'
    print '> '
    choice = STDIN.gets.chomp

    case choice.strip
    when '1'
      print 'Enter a message: '
      msg = STDIN.gets.chomp
      if !msg.match(/\A[a-zA-Z0-9\.!]*\Z/)
        puts 'Invalid message!'
      else
        encrypted_msg = encrypt("puts '#{msg}'", key)
        # encrypted_msg = encrypt(msg, key)
        puts "encrypted_msg: #{encrypted_msg.inspect}"
        puts "Encrypted message: #{encrypted_msg.unpack('H*')[0]}"
      end
    when '2'
      print 'Enter an encrypted command (hex): '
      enc_cmd = STDIN.gets.chomp
      cmd = decrypt([enc_cmd].pack('H*'), key)
      puts "Decrypted command: #{cmd}"
      eval cmd
    else
      puts 'Invalid choice.'
    end
  end
end

main

