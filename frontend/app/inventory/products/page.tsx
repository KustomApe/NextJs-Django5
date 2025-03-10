export default function Page() {
    return(
        <>
            <h2>商品一覧</h2>
            <button>商品を追加する</button>
            <table>
                <thead>
                    <tr>
                        <th>商品ID</th>
                        <th>商品名</th>
                        <th>単価</th>
                        <th>説明</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>コットン100%バックリボンティアードワンピース(黒)</td>
                        <td>6900</td>
                        <td>大人の可愛らしさを引き立てる、ナチュラルな風合い。リラックス×トレンドを楽しめる、上品なティアードワンピース。</td>
                        <td><button>更新・削除</button></td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>ライトストレッチカットソー(ネイビー)</td>
                        <td>2980</td>
                        <td>しなやかな肌触りが心地よい、程よいフィット感のカットソー。ビジネスカジュアルにも普段遣いにも使える、ベーシックなデザイン。</td>
                        <td><button>更新・削除</button></td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>ベルト付きデニムパンツ(ブルー)</td>
                        <td>5980</td>
                        <td>定番のデニムパンツに、フェミニンアベルトをプラスしたスタイリッシュなアイテム。カジュアルにもきれいめにも合わせやすい。</td>
                        <td><button>更新・削除</button></td>
                    </tr>
                </tbody>
            </table>
        </>
    )
}
