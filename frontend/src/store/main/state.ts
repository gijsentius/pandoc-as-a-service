import { Flag } from '@/interfaces'

export interface MainState {
  document: File | undefined,
  files: File[],
  flags: Flag[]
}
