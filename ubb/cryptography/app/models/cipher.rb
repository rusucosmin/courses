class Cipher
  include ActiveModel::Validations
  attr_accessor :alphabet, :alpha, :beta, :text

  def initialize(params={})
    @alphabet = params[:alphabet]
    @alpha = params[:alpha]
    @beta = params[:beta]
    @text = params[:text]
  end

  def encrypt
    ord = {}
    Array(0..alphabet.length - 1).each do |i|
      ord[alphabet[i]] = i
    end
    return text.split('')
      .map{|x| ord[x]}
      .map{|x| (alpha.to_i * x + beta.to_i) % alphabet.length}
      .map{|x| alphabet[x]}
      .join
  end

  def decrypt
    ord = {}
    Array(0..alphabet.length - 1).each do |i|
      ord[alphabet[i]] = i
    end
    inv = invmod alpha.to_i, alphabet.length
    text.split('')
      .map{|x| ord[x]}
      .map{|x| (inv * x - beta.to_i) % alphabet.length}
      .map{|x| alphabet[x]}
      .join
  end

private
  def alpha_and_alphabet_size_should_be_coprime
    if @alphabet && @alpha && @alphabet.length.gcd(@alpha.to_i) != 1
      errors.add(:alpha, "Alpha and alphabet size should be coprime")
      errors.add(:alphabet, "Alpha and alphabet size should be coprime")
    end
  end

  def invmod(x, mod)
    Array(0..mod-1).each do |inv|
      if (inv * x) % mod == 1
        return inv
      end
    end
    "math is broken"
  end

  validates :alphabet, presence: true
  validates :alpha, presence:true, numericality: { only_integer: true }
  validates :beta, presence: true, numericality: { only_integer: true }
  validates :text, presence: true
  validate :alpha_and_alphabet_size_should_be_coprime
end
