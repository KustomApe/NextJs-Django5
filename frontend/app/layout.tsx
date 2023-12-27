import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import './globals.css'
import Navigation from '@/components/auth/Navigation'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Next.JS+DRF入門',
  description: 'Next.JS+DRF入門',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang='ja'>
      <body className='{inter.className}'>
        <div className='flex min-h-screen flex-col'>
          <Navigation />

          <main className='container mx-auto max-w-screen-md flex-1 px-2'>
            { children }
          </main>

          {/* フッター */}
          <footer className='py-5'>
            <div className='text-center text-sm'>
              Copyright &copy; All rights reserved | {' '}
              <a href='https://eisukenakanishi.com'
              target='_blank'
              rel='noopener noreferrer'
              className='underline'
              >AsK
              </a>
            </div>
          </footer>
        </div>
      </body>
    </html>
  )
}
