const env = process.env.VUE_APP_ENV

let envApiUrl = ''

if (env === 'production') {
  console.log(process.env.VUE_APP_DOMAIN_PROD)
  envApiUrl = `https://${process.env.VUE_APP_DOMAIN_PROD}`
} else {
  envApiUrl = `http://${process.env.VUE_APP_DOMAIN_DEV}`
}

export const apiUrl = envApiUrl
