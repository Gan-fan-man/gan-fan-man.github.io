# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "Ganfan_man_Pages"
  spec.version       = "0.1.0"
  spec.authors       = ["Ganfan_man"]
  spec.email         = ["ganfan.man.2023@gmail.com"]

  spec.summary       = "A Jekyll Tool&Post Web Pages"
  spec.homepage      = "https://github.com/Gan-fan-man/gan-fan-man.github.io"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README)!i) }

  spec.add_runtime_dependency "jekyll", "~> 4.4.0"
  spec.add_runtime_dependency "jekyll-feed", "~> 0.17.0"
  spec.add_runtime_dependency "jekyll-seo-tag", "~> 2.8.0"
  spec.add_runtime_dependency "jekyll-gist", "~> 1.5.0"
  spec.add_runtime_dependency "jekyll-paginate-v2", "~> 3.0"
  spec.add_runtime_dependency "jekyll-sitemap", "~> 1.4.0"
  spec.add_runtime_dependency "kramdown-parser-gfm", "~> 1.1"
  spec.add_runtime_dependency "jemoji", "~> 0.13.0"

  spec.add_development_dependency "bundler", "~> 2.4.22"
  spec.add_development_dependency "rake", "~> 13.3.0"
end
