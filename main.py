import streamlit as st
import worldmesh as wm
import folium


def main():
    st.title("Simple Square Calculator")

    meshcode3 = 2052345020

    st.write(f"MESHCODE : {meshcode3}")

    ##地図パート

    latlng_dict = wm.meshcode_to_latlong_grid(meshcode3)
    center_lat, center_lng = (latlng_dict["lat0"] + latlng_dict["lat1"]) / 2, (
        latlng_dict["long0"] + latlng_dict["long1"]
    ) / 2
    google_maps_url = "https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"

    # 地図の初期位置を設定
    m = folium.Map(location=[center_lat, center_lng], zoom_start=15, tiles=None)

    # Google Mapsのタイルレイヤーを追加
    folium.TileLayer(
        tiles=google_maps_url, attr="Google", name="Google Maps", overlay=True
    ).add_to(m)

    # 四角形の座標を指定（南西端と北東端の緯度経度を指定）
    sw = [latlng_dict["lat1"], latlng_dict["long0"]]  # 南西端の緯度経度
    ne = [latlng_dict["lat0"], latlng_dict["long1"]]  # 北東端の緯度経度

    # 四角形を描画
    rectangle = folium.Rectangle(
        bounds=[sw, ne],  # 南西端と北東端の座標を指定
        color="red",  # 枠線の色
        fill=True,  # 塗りつぶしを有効にする
        fill_color="red",  # 塗りつぶしの色
        fill_opacity=0.4,  # 塗りつぶしの透明度
    )

    # 地図に四角形を追加
    rectangle.add_to(m)

    # Streamlitで地図を表示
    # st.folium_static(m)
    st.components.v1.html(folium.Figure().add_child(m).render(), height=500)


if __name__ == "__main__":
    main()
