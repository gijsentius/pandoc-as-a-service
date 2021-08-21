const env = process.env.VUE_APP_ENV

let envApiUrl = ''

if (env === 'production') {
  envApiUrl = `https://${process.env.VUE_APP_DOMAIN_PROD}`
} else {
  console.log('domain-dev: ' + process.env.VUE_APP_DOMAIN_DEV)
  envApiUrl = `http://${process.env.VUE_APP_DOMAIN_DEV}`
}

export const apiUrl = envApiUrl
