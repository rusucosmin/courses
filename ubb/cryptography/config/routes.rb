Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  get '/' => 'application#show'
  get '/encrypt' => 'crypto#encrypt'
  get '/decrypt' => 'crypto#decrypt'
  get '*path' => redirect('/')
end
